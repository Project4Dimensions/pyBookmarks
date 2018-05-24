# pyBookmarks

Research and development: Project4Dimensions

## Why pyBookmarks?

pyBookmarks is a web application to create, retrieve, update and delete
bookmarks using any modern web browser.

See [`bookmarks.py`](bookmarks.py).

## How to use pyBookmarks

Install Python3 and pyBookmarks dependencies. In Debian and Ubuntu Linux,
open a terminal and type  
`sudo apt install python3 python3-pip python3-bottle python3-gevent sqlite3`.

Usage is as follows. Open a terminal, cd to the pyBookmarks folder
and type `python3 -m bookmarks`. Then open a browser using this link:
[`http://localhost:8118/`](http://localhost:8118/).

## Discussion

Switching between web browsers often involves exporting and importing
bookmarks and keeping these up-to-date.

Some web browser bookmark managers lack fields for tags and notes.

pyBookmarks offers a cross-browser solution that can also be used off-line.

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
