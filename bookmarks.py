#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# pyBookmarkss: a web app to create, retrieve, update, and delete bookmarks
# repository: github.com/Project4Dimensions/pyBookmarks

# dependencies (debian, ubuntu):
# sudo apt install python3 python3-pip python3-bottle python3-eventlet sqlite3

# dependencies (macOS, Windows):
# download installer from https://www.python.org/downloads/
# download installer from https://www.sqlite.org/download.html
# pip3 install bottle eventlet

# usage: python3 -m bookmarks

from bottle import request, route, run, static_file, template
import eventlet, os, os.path, re, sqlite3, sys

# @route(r'/docs/<filename:re:.*\.ico>')
# def send_image(filename):
    # # mimetype='image/vnd.microsoft.icon'
    # return static_file(filename, root='/docs', mimetype='image/x-icon')

@route(r'/docs/assets/css/<filepath:re:.*\.css>')
def css(filepath):
    return static_file(filepath, root='docs/assets/css')

@route(r'/docs/assets/fonts/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>')
def font(filepath):
    return static_file(filepath, root='docs/assets/fonts')

@route(r'/docs/assets/images/<filepath:re:.*\.(gif|ico|jpg|png|svg)>')
def img(filepath):
    return static_file(filepath, root='docs/assets/images')

@route(r'/docs/assets/js/<filepath:re:.*\.js>')
def js(filepath):
    return static_file(filepath, root='docs/assets/js')

@route('/docs/<filename:path>')
# def server_static(filepath):
def send_static(filepath):
    return static_file(filepath, root='/docs')

# path to database file
db = 'docs/bookmarks.db'

# path to templates folder
tpl = 'docs/bookmarks/views/'

# title: html head
ttlb = 'Bookmarks » '

@route('/')
def index():
    if os.path.exists(db):
        return template(tpl + 'index', title=ttlb, tpl=tpl)
    else:
        conn = sqlite3.connect(db)
        c = conn.cursor()
        c.execute('CREATE TABLE bookmarks (id INTEGER PRIMARY KEY, title TEXT, uri TEXT, tags TEXT, note TEXT, x INTEGER)')
        c.execute('CREATE INDEX idx_bookmarks_tags ON bookmarks (tags)')
        conn.commit()
        return template(tpl + 'index', title=ttlb, tpl=tpl)

@route('/create', method='GET')
def create():
    if request.GET.create:
        title = request.GET.title.strip()
        uri = request.GET.uri.strip()
        tags = request.GET.tags.strip()
        note = request.GET.note.strip()
        conn = sqlite3.connect(db)
        c = conn.cursor()
        c.execute('INSERT INTO bookmarks (title, uri, tags, note) VALUES (?,?,?,?)', (title, uri, tags, note))
        conn.commit()
        nm = c.lastrowid
        c.execute('SELECT id, title, uri, tags, note FROM bookmarks WHERE id=?', (nm,))
        r = c.fetchone()
        c.close()
        return template(tpl + 'created', row=r, row_id=nm, title=ttlb, tpl=tpl)
    else:
        return template(tpl + 'create', title=ttlb, tpl=tpl)

@route('/retrieve')
def retrieve():
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('SELECT id, title, uri, tags, note FROM bookmarks')
    r = c.fetchall()
    n = len(r) # number of entries retrieved
    c.close()
    return template(tpl + 'retrieved', n=n, rows=r, title=ttlb, tpl=tpl)

@route('/update/:nm', method='GET')
def update(nm):
    if request.GET.update_row:
        title = request.GET.title.strip()
        uri = request.GET.uri.strip()
        tags = request.GET.tags.strip()
        note = request.GET.note.strip()
        conn = sqlite3.connect(db)
        c = conn.cursor()
        c.execute('UPDATE bookmarks SET title=?, uri=?, tags=?, note=? WHERE id=?', (title, uri, tags, note, nm,))
        conn.commit()
        c.execute('SELECT id, title, uri, tags, note FROM bookmarks WHERE id=?', (nm,))
        r = c.fetchone()
        c.close()
        return template(tpl + 'updated', row=r, row_id=nm, title=ttlb, tpl=tpl)
    else:
        conn = sqlite3.connect(db)
        c = conn.cursor()
        c.execute('SELECT title, uri, tags, note FROM bookmarks WHERE id=?', (nm,))
        r = c.fetchone()
        p = '/update/' + str(nm)
        return template(tpl + 'update', old=r, pth=p, title=ttlb, tpl=tpl)

@route('/delete/:nm', method='GET')
def delete(nm):
    if request.GET.delete_row:
        conn = sqlite3.connect(db)
        c = conn.cursor()
        c.execute('SELECT id, title, uri, tags, note FROM bookmarks WHERE id=?', (nm,))
        r = c.fetchone()
        c.execute('DELETE FROM bookmarks WHERE id=?', (nm,))
        conn.commit()
        c.close()
        return template(tpl + 'deleted', row=r, row_id=nm, title=ttlb, tpl=tpl)
    else:
        conn = sqlite3.connect(db)
        c = conn.cursor()
        c.execute('SELECT title, uri, tags, note FROM bookmarks WHERE id=?', (nm,))
        r = c.fetchone()
        p = '/delete/' + str(nm)
        return template(tpl + 'delete', old=r, pth=p, title=ttlb, tpl=tpl)

@route('/search', method='GET')
def search():
    if request.GET.search:
        tags = request.GET.tags.strip()
        conn = sqlite3.connect(db)
        c = conn.cursor()
        c.execute('SELECT id, title, uri, tags, note FROM bookmarks WHERE tags LIKE ?', ('%'+tags+'%',))
        r = c.fetchall()
        n = len(r) # number of entries retrieved
        c.close()
        return template(tpl + 'retrieved', n=n, rows=r, title=ttlb, tpl=tpl)
    else:
        return template(tpl + 'search', title=ttlb, tpl=tpl)

run(host='0.0.0.0', port=8118, server='eventlet', reloader=True, debug=True)
