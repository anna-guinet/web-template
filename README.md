# Web template

Simple and responsive layout to customize for a personal researcher website.
Template available in two versions: pure HTML text editing (`template/`) or with markdown (`template-markdown/`).

Previews available for the different webpages:
- `preview-home.png` is the preview of the home page for laptop-size screens. 
- `preview-home-tablet.png` is the preview of the home page for tablets (iPad). 
- `preview-home-smartphone.png` is the preview of the home page for smartphones (Galaxy S9). 
- `preview-publications.png` is the preview of the list of publications page for laptop-size screens. 
- `preview-presentations.png` is the preview of the presentations page for laptop-size screens. 
- `preview-teaching.png` is the preview of the list of courses page for laptop-size screens. 

## Version 1 HTML editing: Template/ 

Web template written in HTML, CSS and PHP, by Anna Guinet.
Text editing is pure HTML. The code makes it possible to customize every element of the layout.

### Directory structure

- `template` contains the template.
- `template/css` contains the CSS style files.
- `template/img` contains the images loaded on your website.
- `template/slides` contains slides to link to on your website.


## Version 2 Markdown: Template-Markdown/

Adaptation of Version 1 with markdown by Benoît Viguier, without PHP.
This version makes it simpler to edit the text than pure HTML and is easier to read. 
But it makes more difficult to customize the layout. 

### Requirements

- `make` (optional)
- `python3`
- python3 extension: markdown
  > `pip3 install markdown`
- python3 extension: python-markdown-comment
  > `pip3 install python-markdown-comments`


### Directory structure

- `template-markdown` contains the template.
- `template-markdown/css` contains the CSS style files.
- `template-markdown/img` contains the images loaded on your website.
- `template-markdown/includes` contains the header and footer of the website.
- `template-markdown/md` containts markdown sources for the generated files.
- `template-markdown/slides` contains slides to link to on your website.

### Compilation of the website

Execute `make` or `python3 build.py` to generate the HTML files.

### Example

In order to process markdown in HTML tags, add `markdown="1"`. This latter attribute is removed when compiling.

```
<div markdown="1">
This markdown is processed. You only see the following list to edit:

- list item 1
- list item 2
</div>

<div>
### This will not be processed.
</div>
```
