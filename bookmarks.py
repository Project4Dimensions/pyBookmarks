#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# pyBookmarks is a web app to create, retrieve, update and delete bookmarks
# repository: github.com/Project4Dimensions/pyBookmarks

# dependencies: python3 python3-pip python3-bottle python3-gevent sqlite3
# usage: python3 -m bookmarks

import os, sqlite3
from gevent import monkey; monkey.patch_all()
from time import sleep
from bottle import request, route, run, static_file, template

@route('/docs/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='docs')

@route('/')
def index():
    if os.path.exists('bookmarks.db'):
        return template('docs/views/index')
    else:
        conn = sqlite3.connect('bookmarks.db')
        c = conn.cursor()
        c.execute('CREATE TABLE bookmarks (id INTEGER PRIMARY KEY, subject TEXT, uri TEXT, tags TEXT, note TEXT, x INTEGER)')
        c.execute('CREATE INDEX idx_bookmarks_tags ON bookmarks (tags)')
        conn.commit()
        return template('docs/views/index')

@route('/create', method='GET')
def create():
    if request.GET.create:
        subject = request.GET.subject.strip()
        uri = request.GET.uri.strip()
        tags = request.GET.tags.strip()
        note = request.GET.note.strip()
        conn = sqlite3.connect('bookmarks.db')
        c = conn.cursor()
        c.execute('INSERT INTO bookmarks (subject, uri, tags, note) VALUES (?,?,?,?)', (subject, uri, tags, note))
        conn.commit()
        nm = c.lastrowid
        c.execute('SELECT id, subject, uri, tags, note FROM bookmarks WHERE id=?', (nm,))
        r = c.fetchone()
        c.close()
        return template('docs/views/created', row=r, row_id=nm)
    else:
        return template('docs/views/create')

@route('/retrieve')
def retrieve():
    conn = sqlite3.connect('bookmarks.db')
    c = conn.cursor()
    c.execute('SELECT id, subject, uri, tags, note FROM bookmarks')
    r = c.fetchall()
    c.close()
    return template('docs/views/retrieved', rows=r)

@route('/update/:nm', method='GET')
def update(nm):
    if request.GET.update_row:
        subject = request.GET.subject.strip()
        uri = request.GET.uri.strip()
        tags = request.GET.tags.strip()
        note = request.GET.note.strip()
        conn = sqlite3.connect('bookmarks.db')
        c = conn.cursor()
        c.execute('UPDATE bookmarks SET subject=?, uri=?, tags=?, note=? WHERE id=?', (subject, uri, tags, note, nm,))
        conn.commit()
        c.execute('SELECT id, subject, uri, tags, note FROM bookmarks WHERE id=?', (nm,))
        r = c.fetchone()
        c.close()
        return template('docs/views/updated', row=r, row_id=nm)
    else:
        conn = sqlite3.connect('bookmarks.db')
        c = conn.cursor()
        c.execute('SELECT subject, uri, tags, note FROM bookmarks WHERE id=?', (nm,))
        r = c.fetchone()
        p = '/update/' + str(nm)
        return template('docs/views/update', old=r, pth=p)

@route('/delete/:nm', method='GET')
def delete(nm):
    if request.GET.delete_row:
        conn = sqlite3.connect('bookmarks.db')
        c = conn.cursor()
        c.execute('SELECT id, subject, uri, tags, note FROM bookmarks WHERE id=?', (nm,))
        r = c.fetchone()
        c.execute('DELETE FROM bookmarks WHERE id=?', (nm,))
        conn.commit()
        c.close()
        return template('docs/views/deleted', row=r, row_id=nm)
    else:
        conn = sqlite3.connect('bookmarks.db')
        c = conn.cursor()
        c.execute('SELECT subject, uri, tags, note FROM bookmarks WHERE id=?', (nm,))
        r = c.fetchone()
        p = '/delete/' + str(nm)
        return template('docs/views/delete', old=r, pth=p)

@route('/search', method='GET')
def search():
    if request.GET.search:
        tags = request.GET.tags.strip()
        conn = sqlite3.connect('bookmarks.db')
        c = conn.cursor()
        c.execute('SELECT id, subject, uri, tags, note FROM bookmarks WHERE tags LIKE ?', ('%'+tags+'%',))
        retrieved = c.fetchall()
        c.close()
        return template('docs/views/retrieved', rows=retrieved)
    else:
        return template('docs/views/search')

run(host='localhost', port=8118, server='gevent', reloader=True, debug=True)
