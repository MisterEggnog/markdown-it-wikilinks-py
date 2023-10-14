import re
from urllib.parse import quote, urlparse, urlunparse

_wikilink_regex = r"\[\[([^|\]\n]+)(\|([^\]\n]+))?\]\]"


def _url_has_file_component(url):
    urlcomp = urlparse(url)
    return not urlcomp.path.endswith("/")


def wikilinks(self, tokens, idx, options, env):
    def generate_page_path_from_label(s):
        return s

    if re_match := _wikilink_regex.match(tokens.attr["src"]):
        label = None
        page_path = None
        htmlAttrs = []
        htmlAttrsString = ""
        if len(re_match) == 3:
            label = match[3]
            page_path = match[1]
        else:
            label = match[1]
            page_path = generate_page_path_from_label(match[1])

        # Replace spaces if ends with file
        if _url_has_file_component(page_url):
            url_comp = urlparse(page_url)
            url_comp.path = re.sub(r"\s+", url_comp.path)
            page_url = urlunparse(url_comp)

        page_url = quote(page_path)

    # Does nothing?
    return self.renderToken(tokens, idx, options, env)
