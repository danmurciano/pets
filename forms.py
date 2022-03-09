from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import InputRequired, URL, Optional, NumberRange


class AddPetForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired(message="Name can't be blank")])
    species = StringField("Species", validators=[InputRequired(message="Species can't be blank")])
    image_url = StringField("Image URL", validators=[Optional(), URL(require_tld=False, message="Please enter a valid URL")])
    age = IntegerField("Age", validators=[ NumberRange(min=0, max=30, message="Age must be between 0 and 30")])
    notes = StringField("Notes")

class EditPetForm(AddPetForm):
    available = BooleanField("Available")
