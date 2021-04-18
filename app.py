# Elijah Thomas
# 4/19/2021
# Treehouse Python Techdegree Project 5
# Learning Journal Web App

"""
I'm going for meets expectations this time. I usually go for exceeds, but flask
has proven extremely complicated compared to my previous projects and I'm
nearing the end of my time allotment to complete the techdegree. Either way,
I'm proud of my code and I think it's very solid.
"""

import forms
import models
import datetime

from peewee import IntegrityError

from flask import (
    flash,
    Flask,
    redirect,
    render_template,
    request,
    url_for
)

app = Flask(__name__)
app.secret_key = "oiu34whta0puiwfvnaesiprb4ug43wguio4w3egjk"

"""
SMALL ISSUE: I wasn't able to use a virtualenv for this project. I checked my
previous project, and it turns out that every virtualenv on my computer stopped
working for some reason. I searched through forums for hours but nothing seemed
to work. The packages (peewee and flask) are instead installed as global
packages on my computer. However, my requirements.txt file reflects all needed
packages and their present versions, so that shouldn't be too much of a
problem. I assume it happened because of some unforseen python update or such.
"""

errmsg = """One or more entries was invalid, probably the date you entered or
 your number of hours. Please correct it and try again."""


@app.before_request
def beforeRequest():
    """Runs before each request"""
    models.db.connect()


@app.after_request
def afterRequest(response):
    """Runs after each request, returns response object"""
    models.db.close()
    return response


@app.route('/')
def index():
    """
    One of the 2 routes to the home page

    Since strftime is used twice within the HTML, I decided to send the entire
    function to the template for reusability.
    """
    return render_template('index.html',
                           db=models.Entry.select()
                           .order_by(models.Entry.date),
                           strftime=datetime.datetime.strftime)


@app.route('/entries')
def entries():
    """Identical to the / route"""
    return render_template('index.html',
                           db=models.Entry.select()
                           .order_by(models.Entry.date),
                           strftime=datetime.datetime.strftime)


@app.route('/entries/new', methods=['POST', 'GET'])
def new():
    """
    The new route. It's already connected to the database via the
    @app.before_request function. All data within the model, except for the
    model's ID, is user-defined. Date and time are respectively confined to the
    datetime and integer types. If either an integrity error (which is what
    would happen if time is not an acceptable integer) happens or the HTTP
    method is POST and the form fails to validate (likely due to an improper
    date format) the user will be flashed an error message.
    """
    form = forms.EntryForm()
    if form.validate_on_submit():
        try:
            models.Entry.create(
                title=form.title.data,
                date=form.date.data,
                time=form.time.data,
                learned=form.learned.data,
                resources=form.resources.data
            )
            flash("Entry saved!")
            return redirect(url_for('index'))
        except IntegrityError:
            flash(errmsg)
    elif request.method == "POST":
        flash(errmsg)
    return render_template('new.html', form=form)


@app.route('/entries/<int:ID>')
def detail(ID):
    """
    Renders the detail template in a very similar way to the homepage. Passes
    in the strftime function for the same reasons. Only passes in a single
    entry from the database, as defined by the ID number in the URL.
    """
    return render_template('detail.html',
                           entry=models.Entry.get_by_id(ID),
                           strftime=datetime.datetime.strftime)


@app.route('/entries/<int:ID>/edit', methods=['POST', 'GET'])
def edit(ID):
    """
    Allows the user to edit an entry using most of the same syntax as the "new"
    route, except the create query is replaced by an update query, as is the
    attached flash message. The first if statement decides whether or not to
    pre-populate the textarea fields on the WTForm. These must be prepopulated
    in the Python file itself for some reason, while all other field types can
    be prepopulated inside the HTML template returned by this function. The
    date is also prepopulated inside the app file because doing it in the HTML
    template will give it an incorrect format. Flash messages are sent to the
    user on the same basis as in the "new" route.
    """
    entry = models.Entry.get_by_id(ID)
    form = forms.EntryForm()
    if request.method == "GET":
        form.date.data = entry.date
        form.learned.data = entry.learned
        form.resources.data = entry.resources
    if form.validate_on_submit():
        try:
            models.Entry.update(
                title=form.title.data,
                date=form.date.data,
                time=form.time.data,
                learned=form.learned.data,
                resources=form.resources.data
            ).where(models.Entry.ID == entry.ID).execute()
            flash("Entry updated!")
            return redirect(url_for('index'))
        except IntegrityError:
            flash(errmsg)
    elif request.method == "POST":
        flash(errmsg)
    return render_template('edit.html',
                           entry=entry,
                           form=form)


@app.route('/entries/<int:ID>/delete')
def delete(ID):
    """
    Very simple. Deletes the record with an ID equal to the one passed to the
    URL, sends a flash message and redirects the user to the homepage where
    they'll see the message.
    """
    models.Entry.get_by_id(ID).delete_instance()
    flash("Entry deleted!")
    return redirect(url_for("index"))

"""
I disabled the reloader. It was causing dependency issues that were way over my
head, and I saw on stack exchange that disabling the reloader might help. All
the same, the program should work fine.
"""

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8000)
