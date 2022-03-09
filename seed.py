from models import db, Pet
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

mick = Pet(name="Mick", species="Dog", image_url="https://ggsc.s3.amazonaws.com/images/uploads/The_Science-Backed_Benefits_of_Being_a_Dog_Owner.jpg", age="4", notes="Well behaved")
ting = Pet(name="Ting Yen", species="Cat", image_url="https://149366108.v2.pressablecdn.com/wp-content/uploads/2019/03/Screen-Shot-2019-03-19-at-8.32.11-AM.png", age="1", notes="Cheerful")
ricardo = Pet(name="Ricardo", species="Monkey", image_url="https://media.npr.org/assets/img/2012/09/13/lesula-c5e409b5f067a26cf77f040aec4620356d76cd7c-s1100-c50.jpg", age="7", notes="Tends to worry too much")

db.session.add(mick)
db.session.add(ting)
db.session.add(ricardo)
db.session.commit()
