import re

_wikilink_regex = r"\[\[([^|\]\n]+)(\|([^\]\n]+))?\]\]"


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
            pagePath = match[1]
        else:
            label = match[1]
            pagePath = generate_page_path_from_label(match[1])
    # Does nothing?
    return self.renderToken(tokens, idx, options, env)
