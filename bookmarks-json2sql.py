#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# pyBookmarks
# create, retrieve, update and delete bookmarks
# repository: github.com/Project4Dimensions/pyExamples

# dependencies (debian, ubuntu):
# sudo apt install python3 sqlite3

# dependencies (macOS, Windows):
# download installer from https://www.python.org/downloads/
# download installer from https://www.sqlite.org/download.html

# usage:
# python3 -m bookmarks-json2sql
# sqlite3 bookmarks.db < "docs/bookmarks/sql/bookmarks.sql"

import json, os, sqlite3

sql_file  = './docs/bookmarks/sql/bookmarks.sql'
json_file = './docs/bookmarks/json/bookmarks.json'

if os.path.exists(sql_file):
    print('ho ho')
    #os.chdir('docs/sql')
    os.remove(sql_file)

if os.path.exists(json_file):
    print('ho ho')
    sql_file = open(sql_file, 'a+', newline='\n')
    json_file = open(json_file, 'r')
    json_string = json_file.read()
    json_string = json_string.replace('\n', '')
    json_string = json_string.replace('\'', '')
    parsed_json = json.loads(json_string)['children'][0]['children']
    posn = 0
    totl = len(parsed_json)
    print('# usage: \n')
    sql_file.write('/* usage: sqlite3 bookmarks.db < "docs/bookmarks/sql/bookmarks2sql.sql" */\n\n')
    print('CREATE TABLE bookmarks (id INTEGER PRIMARY KEY, title TEXT, uri TEXT, tags TEXT, note TEXT, x INTEGER)\n')
    sql_file.write('CREATE TABLE bookmarks (id INTEGER PRIMARY KEY, title TEXT, uri TEXT, tags TEXT, note TEXT, x INTEGER);\n\n')
    print('CREATE INDEX idx_bookmarks_tags ON bookmarks (tags)\n')
    sql_file.write('CREATE INDEX idx_bookmarks_tags ON bookmarks (tags);\n\n')
    print('INSERT INTO bookmarks (title, uri, tags, note) VALUES\n')
    sql_file.write('INSERT INTO bookmarks (title, uri, tags, note) VALUES\n')
    for each in parsed_json:
        posn = posn + 1
        if posn == totl:
            rbrc = ');'
        else:
            rbrc = '),\n'
        title = '\'' + each['title'] + '\',\n'
        uri  = '\'' + each['uri'] + '\',\n'
        if 'tags' in list(each.keys()):
            tagd = each['tags']
        else:
            tagd = ''
        if 'keyword' in list(each.keys()):
            keyw  = ' ' + each['keyword']
        else:
            keyw = ''
        tags = '\'' + tagd + keyw + '\',\n'
        if 'annos' in list(each.keys()):
            note  = '\'' + each['annos'][0]['value'] + '\'\n'
        else:
            note = '\'\'\n'
        print('(\n' + title + uri + tags + note.replace('\\n', '\n') + rbrc)
        sql_file.write('(\n' + title + uri + tags + note.replace('\\n', '\n') + rbrc)
    json_file.close()
    sql_file.close()
else:
    print('Nothing to do!')

# http://docs.python-guide.org/en/latest/scenarios/json/
# json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
# parsed_json = json.loads(json_string)
# print(parsed_json['first_name'])
