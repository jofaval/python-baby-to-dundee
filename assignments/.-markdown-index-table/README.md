# Markdown Index Generator #

_From [https://github.com/jofaval/utilities/issues/3](https://github.com/jofaval/utilities/issues/3)_

Currently, whenever I'm creating/modifying a README, I'm almost all of the time creating/updating and index, while when adding or removing a section, updating even, is not as tedious, creating a bunch of sections and then updating the README, with the indentation level, it's kind of a pain in the booty. Something I could automate.

My idea is that it can generate the index in a separate file, as to not bother myself too much with replacing it's content.

But, as an improvement, or idea even, I could define a region (as with dot.net):
```markdown
<!-- [index-start] -->

1. [Title](#title)
2. [Product](#product)
    1. [Product Roadmap](#product-roadmap)

<!-- [index-end] -->
```

### Example user call

```shell
python3 markdown-index-generator.py --indent-level=3
```

**_indent-level_** being the max indent level you want to index. `0` by default which would mean, every single level

### Optional

- Create a configuration file and implement an observer so that the index cn be automatically taken care of while you're writting docs?
- Adding a back to index, contents
- As an extra, make it indent sensitive, meaning, only first level gets a reference to the contents index table, the rest get a reference (Back to...) the parent's section

### Proposed regex

```regex
/[\w\s]+/igu
```