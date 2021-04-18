# Treehouse-Python-Techdegree-Project-5
A simple (but solid) web app designed to keep and alter detailed records about what the user has learned. Makes extensive use of Flask and the Peewee ORM.

I viewed some of my Treehouse coursework and some Stack Exchange forums to do my debugging, but all this code is original.

Only a few minor adjustments have been made to the HTML, like moving the files to a templates directory and then changing the hrefs to the CSS files to account for the directory changes, as well as adding a small readout on the index, new and edit HTML files that displays the current flash message. All example content has been replaced with templates.

Users are able to:
  - Create records
  - Edit records in their entirety (all 5 fields)
  - Delete records

Records are selected by their Peewee-given ID number, which also functions as their primary key within the database.

In-depth descriptions of all functions and classes in app.py and the two modules are included in docstrings.

Code is PEP-8 compliant according to http://pep8online.com/
