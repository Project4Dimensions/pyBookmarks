# pyBookmarks

Research and development: Project4Dimensions

## Why pyBookmarks?

Switching between web browsers often involves exporting and importing
bookmarks and keeping these up-to-date.

Some web browser bookmark managers lack fields for tags and notes.

pyBookmarks offers a cross-browser solution that can also be used off-line.
Use this web application to create, retrieve, update, and delete bookmarks
using any modern web browser.

The Browse Happy website suggests suitable browsers.  
[`https://browsehappy.com/`](https://browsehappy.com/)

See [`bookmarks.py`](bookmarks.py).

## How to use pyBookmarks

Install Python3 and pyBookmarks dependencies.

For Debian and Ubuntu Linux, open a terminal and type the following:  
`sudo apt install python3 python3-pip python3-bottle python3-eventlet sqlite3`.

For macOS and Windows, download installers from the following websites:  
[`https://www.python.org/downloads/`](https://www.python.org/downloads/)  
[`https://www.sqlite.org/download.html`](https://www.sqlite.org/download.html)  

In macOS and Windows, open a terminal and type  
`pip3 install bottle eventlet`

For Android, install and open Termux; then type  
`pgk update`  
`pgk upgrade`  
`pkg install sqlite python3`  
`python3 -m pip install --upgrade pip`  
`pip install bottle`  
`pip install eventlet`

Usage is as follows below.

Open a terminal, cd to the pyBookmarks folder and type    
`python3 -m bookmarks`

In a web browser, paste and go to this link:  
[`http://localhost:8118`](http://localhost:8118/)

To import Firefox bookmarks, read this file:  
[`bookmarks-json2sql.md`](bookmarks-json2sql.md).

## References

Hellkamp, Marcel. 2018.  
“Tutorial — Bottle 0.13-dev documentation.”  
*Bottle 0.13-dev*. May 22.  
[http://bottlepy.org/docs/dev/tutorial.html][1].

[1]: http://bottlepy.org/docs/dev/tutorial.html

Popov, Dmitri. 2015.  
“Python in a Bottle: Using the Bottle framework to build Python apps.”  
*Linux Magazine* 174 (May).  
[http://www.linux-magazine.com/Issues/2015/174/Workspace-Bottle][2].

[2]: http://www.linux-magazine.com/Issues/2015/174/Workspace-Bottle

Schnelle, Jochen. 2018.  
“Tutorial: Todo-List Application — Bottle 0.13-dev documentation.”  
*Bottle 0.13-dev*. May 22.  
[https://bottlepy.org/docs/dev/tutorial_app.html][3].

[3]: https://bottlepy.org/docs/dev/tutorial_app.html
