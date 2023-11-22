Pile of spaghetti loosely ported from jsepia/markdown-it-wikilinks.

Currently this fails when there are more than one wikilink in a paragraph. This means strings such as `"[[left]] [[right]]"` will only parse `[[left]]`. If this is an issue use a different markdown library.
