Pile of spaghetti loosely ported from jsepia/markdown-it-wikilinks.

Currently this fails when there are more than one wikilink in a paragraph. This means strings such as `"[[left]] [[right]]"` will only parse `[[left]]`. If this is an issue use a different markdown library.

The documentation for markdown-it is terrible, there is little in the way of online guides to write plugins, & the documentation itself incredibly sparse. There are few communities online you can look for help & the only community I found is empty with unanswered questions.
