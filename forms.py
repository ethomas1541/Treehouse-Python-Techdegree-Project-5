from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import (
    DateField,
    IntegerField,
    StringField,
    TextAreaField
)


class EntryForm(FlaskForm):
    """
    Pretty simple WTForm for use when adding/editing new database records.

    Form will fail to validate if the date is formatted improperly or the
    time in hours is not an integer.
    """
    title = StringField(
        "Title",
        validators=[DataRequired()]
    )
    date = DateField(
        "Date (MM-DD-YYYY)",
        validators=[DataRequired()],
        format="%m-%d-%Y"
    )
    time = IntegerField(
        "Time spent (Hours)",
        validators=[DataRequired()]
    )
    learned = TextAreaField(
        "What did you learn?",
        validators=[DataRequired()]
    )
    resources = TextAreaField(
        "Did you use any resources you want to remember?",
        validators=[DataRequired()]
    )
