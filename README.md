Pile of spaghetti loosely ported from jsepia/markdown-it-wikilinks.

Currently this fails when there is more than one wikilink in a paragraph. This means strings such as `"[[left]] [[right]]"` will only parse `[[left]]`. If this is an issue use a different markdown library, it is unlikely I will continue on this.

The documentation for markdown-it is terrible, there is little in the way of online guides to write plugins, & the documentation itself is incredibly sparse. There are few communities online you can look for help in & the only community I found is empty with unanswered questions. This combined with the immaturity of some of the [javascript developers], has turned me off from this library entirely. I have since switched to use [markdown], which has this functionality builtin.

[javascript developers]: https://github.com/markdown-it/markdown-it/issues/10
[markdown]: https://python-markdown.github.io/
