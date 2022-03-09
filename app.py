from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["SECRET_KEY"] = "w57h63ff9"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route("/")
def list_pets():
    pets = Pet.sort()
    return render_template("home.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        if request.form["image_url"] != "":
            image_url = request.form["image_url"]
        else:
            image_url = None
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(name=name, species=species, image_url=image_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"Added {name} to pets")
        return redirect("/")

    else:
        return render_template("add-pet.html", form=form)



@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        if request.form["image_url"] != "":
            pet.image_url = request.form["image_url"]
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"Updated {pet.name}")
        return redirect("/")

    else:
        return render_template("edit-pet.html", pet=pet, form=form)
