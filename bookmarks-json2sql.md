# pyBookmarks bookmarks-json2sql

## Why bookmarks-json2sql?

Use the Python script to convert Firefox JSON backup bookmarks to SQL.
   
See [`bookmarks-json2sql.py`](bookmarks-json2sql.py).

## How to use bookmarks-json2sql

In Firefox, open `Manage Bookmarks`.
Organize bookmarks as shown in the image below

[`docs/assets/images/firefox-bookmarks.png`](docs/assets/images/firefox-bookmarks.png)

In the `Manage Bookmarks` window, click on `Import and Backupˇ Backup…`;  
save as bookmarks.json in the pyBookmarks `docs/bookmarks/json` folder.  
Open another terminal window, cd to the pyBookmarks folder and type  
`python3 -m bookmarks-json2sql`

## Reference

Reitz, Kenneth and Real Python. n.d.  
    “JSON — The Hitchhiker's Guide to Python.”  
    Accessed January 25, 2023.  
    [https://docs.python-guide.org/scenarios/json/][1].

[1]: https://docs.python-guide.org/scenarios/json/
