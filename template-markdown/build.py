#!/usr/bin/env python3

import markdown
from python_markdown_comments import CommentsExtension
from os import listdir
import datetime

def save(fn, z):
    d = open(fn, 'w', encoding="utf-8")
    d.write(z)
    d.close()


def load(fn):
    d = open(fn, 'r', encoding="utf-8")
    z = d.read()
    d.close()
    return z

def trim_comment(str):
    idx = str.find('<!--')
    if idx > 0:
        str = str[0:idx]
    return str

########################################
#
#		PARSING AND EXPORTING
#
########################################
def main():
    # load config
    config = ""
    try:
        config = load('.config')
        config = config.split('\n')
    except:
        print('.config not found')

    name = "Jane Smith"
    title = "Tech Support Consultant"
    entity = "I-Temp Technology Staffing"

    if len(config) > 0:
        name = config[0]
        name = trim_comment(name)
    if len(config) > 1:
        title = config[1]
        title = trim_comment(title)
    if len(config) > 2:
        entity = config[2]
        entity = trim_comment(entity)
    
    # load markdown parser
    comments = CommentsExtension()
    md = markdown.Markdown(extensions=['extra', comments, 'md_in_html'])
    
    # load header and footer
    header = load('includes/header.html')
    footer = load('includes/footer.html')

    header = header.format(name=name, title=title, entity=entity)

    # load pages
    pages = listdir('md')
    for pagesfile in pages:
        if pagesfile[-3:] == '.md':
            file_in = load('md/' + pagesfile)
            # check if the file starts with '<div class="main'
            main_class_found = file_in[:16] == '<div class="main'

            # start with header
            html = header

            # begin content
            html += "\n<div class='content'>\n"
            if not main_class_found:
                html += "\t<div class='main'>\n"

            # convert markdown into html
            html += md.convert(file_in)

            if not main_class_found:
                html += "\n\t</div>"

            # close content
            html += "\n</div>\n"

            #close with footer
            today = datetime.datetime.now()
            html += footer.format(today=today.strftime("%B %d, %Y"))

            # save file
            file_out = pagesfile[0:-3] + '.html'
            save(file_out, html)

    print("\tBuild completed !")

main()
