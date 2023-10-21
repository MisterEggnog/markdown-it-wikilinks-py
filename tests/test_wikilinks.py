import pytest
from markdown_it import MarkdownIt
from markdown_it_wikilinks import wikilinks
import markdown_it_wikilinks as md_wikilinks

examples = [
    ("[[Wiki Link]]", '<p><a href="./Wiki_Link.html">Wiki Link</a></p>'),
    ("[[Help/Wiki Link]]", '<p><a href="./Help/Wiki_Link.html">Help/Wiki Link</a></p>'),
    (
        "[[/Main/Wiki Link]]",
        '<p><a href="/Main/Wiki_Link.html">/Main/Wiki Link</a></p>',
    ),
    (
        "Here is a [[Wiki Link]]",
        '<p>Here is a <a href="./Wiki_Link.html">Wiki Link</a></p>',
    ),
    (
        "[[Wiki Link with multiple spaces]]",
        '<p><a href="./Wiki_Link_with_multiple_spaces.html">Wiki Link with multiple spaces</a></p>',
    ),
    (
        "[[Wiki Link]]s with trailing letters",
        '<p><a href="./Wiki_Link.html">Wiki Link</a>s with trailing letters</p>',
    ),
    (
        "[[Feline hypercuteness#Signs and symptoms]] with anchor",
        '<p><a href="./Feline_hypercuteness.html#Signs_and_symptoms">Feline hypercuteness</a> with anchor</p>',
    ),
    (
        "[[/Main/Feline hypercuteness#Signs and symptoms]] with path and anchor",
        '<p><a href="/Main/Feline_hypercuteness.html#Signs_and_symptoms">/Main/Feline hypercuteness</a> with path and anchor</p>',
    ),
    (
        "Click [[Wiki Link|here]] to learn about wiki links",
        '<p>Click <a href="./Wiki_Link.html">here</a> to learn about wiki links</p>',
    ),
    (
        'Also, [[Wiki.Link|Wiki "Links" can use punctuation!]]',
        '<p>Also, <a href="./Wiki.Link.html">Wiki "Links" can use punctuation!</a></p>',
    ),
    (
        "[[Wiki Link#anchor-name|This link]] has both an anchor and an alias",
        '<p><a href="./Wiki_Link.html#anchor-name">This link</a> has both an anchor and an alias</p>',
    ),
    (
        "This is a [[Hyphenated-Wiki-Link]]",
        '<p>This is a <a href="./Hyphenated-Wiki-Link.html">Hyphenated-Wiki-Link</a></p>',
    ),
    (
        "This is an [[#Anchor_only_link]]",
        '<p>This is an <a href="#Anchor_only_link">Anchor_only_link</a></p>',
    ),
    ("This is [[not a valid wiki link]", "<p>This is [[not a valid wiki link]</p>"),
    (
        "This is [not a valid wiki link]] either",
        "<p>This is [not a valid wiki link]] either</p>",
    ),
    (
        "This is also not a valid wiki link: [[]]",
        "<p>This is also not a valid wiki link: [[]]</p>",
    ),
]


@pytest.mark.skip(reason="Not yet implemented")
@pytest.mark.parametrize("input,expected", examples)
def test_wikilink_examples(input, expected):
    markdown = MarkdownIt()
    markdown.add_render_rule("text", wikilinks)
    assert expected == markdown.render(input)


def test_render_rule_runs():
    markdown = MarkdownIt()
    markdown.add_render_rule("text", wikilinks)
    markdown.render("[[this does not matter]]")


def test_url_has_file_component():
    assert md_wikilinks._url_has_file_component(
        "https://www.egg.spam/dink"
    ), "link is bare file"
    assert not md_wikilinks._url_has_file_component(
        "https://www.egg.spam/dink/"
    ), "link is a directory"


def test_post_process_path():
    path = "/lol       "
    assert md_wikilinks.post_process_page_path(path) == "/lol"
    path = "spam and eggs"
    assert md_wikilinks.post_process_page_path(path) == "spam_and_eggs"
