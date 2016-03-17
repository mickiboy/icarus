#!/bin/env python3
#
# icarus cms
#
# (c) 2016 Daniel Jankowski

import os
import re
import json
import time

import util
import html_items

from util import *

#############
# MAIN SITE #
#############

def generate_archive(dates):
    archive = ""
    for d in dates:
        a = get_month(d)
        if a not in archive:
            archive += ('<li><a href="">{title}</a></li>'.format(title=str(a) + ' ' + str(re.sub(r'(.*)\-(.*)\-(.*)', r'\1', d)) ))
    return archive


def build_main_site(title, stylesheet, articles):
    out = html_items.get_header(title, stylesheet)
    sidebar_t, sidebar_a = "", []

    # generate main cards
    for ar in articles:
        a = ar[0]
        out += html_items.get_blog_card(a["title"], a["content"], a["author"], "{day} {month} {year}".format(
                day=re.sub(r'(.*)\-(.*)\-(.*)$', r'\3', a["date"]),
                month=get_month(a["date"]),
                year=re.sub(r'(.*)\-(.*)\-(.*)$', r'\1', a["date"])
            ), generate_filename(ar[1], a["title"]))

    # generate sidebar
    out += build_sidebar(articles)

    # generate footer
    out += html_items.get_footer()

    # write html to file
    write_html("../static/index.html", out)
    return out


###################
# SINGLE ARTICLES #
###################

def build_articles(title, stylesheet, articles):
    sidebar = build_sidebar(articles)

    for ar in articles:
        a = ar[0]
        out = html_items.get_header(title, stylesheet)
        out += html_items.get_article_card(a["title"], a["content"], a["author"], "{day} {month} {year}".format(
                day=re.sub(r'(.*)\-(.*)\-(.*)$', r'\3', a["date"]),
                month=get_month(a["date"]),
                year=re.sub(r'(.*)\-(.*)\-(.*)$', r'\1', a["date"])
            ))
        out += sidebar
        out += html_items.get_footer()
        write_html('../static/' + generate_filename(ar[1], a['title']), out)
    pass


#########
# UTILS #
#########

def generate_filename(date, title):
    return "{date}-{title}.html".format(
            date=re.sub('\s|:', '_', str(date)),
            title=title
            )


def build_sidebar(articles):
    counter = 0
    sidebar_t, sidebar_a = "", []
    for ar in articles:
        a = ar[0]
        if counter < 10:
            sidebar_t += '<li><a href="{url}">{title}</a></li>'.format(title=a["title"], url=generate_filename(ar[1], a["title"]))
        sidebar_a.append(a["date"])
        counter += 1

    # generate sidebar
    return html_items.get_sidebar(sidebar_t, generate_archive(sidebar_a))


def fetch_articles(directory):
    if not os.path.exists(directory):
        return [] # TODO: Error handling
    files, content = os.listdir(directory), []
    for f in files:
        if not os.path.isfile(directory + f):
            continue
        if f.endswith('.json'):
            with open(directory + f) as fp:
                content.append((json.load(fp), time.ctime(os.stat(os.path.join(directory, f)).st_ctime)))
    return content


def main():
    log('module test\n')

    log('fetching articles')
    content = fetch_articles('../articles/')
    content = sorted(content, key=lambda content: content[1], reverse=True)
    log('generate main site')
    build_main_site('icarus', 'default.css', content)
    log('generate articles')
    build_articles('icarus', 'default.css', content)
    print()
    log('Success!')
    pass


if __name__ == '__main__':
    main()
