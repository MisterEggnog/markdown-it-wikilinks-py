import re
from urllib.parse import quote, urlparse, urlunparse

_wikilink_regex = re.compile(r"\[\[([^|\]\n]+)(\|([^\]\n]+))?\]\]")


def _url_has_file_component(url):
    urlcomp = urlparse(url)
    return not urlcomp.path.endswith("/")


def post_process_page_path(page_path):
    page_path = page_path.strip()
    page_path = re.sub(r"\s+", "_", page_path)
    return page_path


def post_process_fragment(fragment):
    return post_process_page_path(fragment)


def generate_page_path_from_label(s):
    return s


def _process_wikilink_regex(token, re_match):
    left_patch = token.content[: re_match.span()[0]]
    right_patch = token.content[re_match.span()[1] :]

    label = None
    page_path = None
    htmlAttrs = []
    htmlAttrsString = ""
    if re_match.group(2) is not None:
        label = re_match[3]
        page_path = re_match[1]
    else:
        label = re_match[1]
        page_path = generate_page_path_from_label(re_match[1])

    page_url = page_path
    url_comp = urlparse(page_url)

    # Replace spaces if ends with file
    url_comp = url_comp._replace(path=post_process_page_path(url_comp.path))
    if not url_comp.path.endswith("/"):
        url_comp = url_comp._replace(path=url_comp.path + ".html")
    if not url_comp.path.startswith("/"):
        url_comp = url_comp._replace(path="./" + url_comp.path)
    url_comp = url_comp._replace(path=quote(url_comp.path))

    # Sanitize fragment if it exists
    if url_comp.fragment is not None:
        url_comp = url_comp._replace(fragment=post_process_fragment(url_comp.fragment))
        url_comp = url_comp._replace(fragment=quote(url_comp.fragment))

    page_url = urlunparse(url_comp)
    escapedHref = page_url
    htmlAttrsString = f'href="{escapedHref}"'
    label = label.split("#")[0]

    return f"{left_patch}<a {htmlAttrsString}>{label}</a>{right_patch}"


def wikilinks(self, tokens, idx, options, env):
    token = tokens[idx]

    if re_match := _wikilink_regex.search(token.content):
        return _process_wikilink_regex(token, re_match)

    # This doesn't feel right
    return token.content
    # return self.renderToken(tokens, idx, options, env)
