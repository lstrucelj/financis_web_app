from pony.orm import Database, PrimaryKey, Required, Set, db_session, Optional
from uuid import uuid4
import os


db = Database()

# ukoliko želiš da se svaki puta briše baza
# if os.path.exists("database.sqlite"):
#    os.remove("database.sqlite")

db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

class Korisnik(db.Entity):
    id = PrimaryKey(str, default=lambda: str(uuid4().hex))
    ime = Required (str)
    prezime = Required (str)
    email = Required (str)
    lozinka = Required (str)
    troskovi = Optional("Trosak")

class Trosak(db.Entity):
    id = PrimaryKey(str, default=lambda: str(uuid4().hex))
    naziv = Required (str)
    kategorija = Required (str)
    iznos = Required (int)
    korisnik = Required (Korisnik)

db.generate_mapping(create_tables=True, check_tables=True)


if __name__ == "__main__":
    with db_session() as s:
        u = Trosak(naziv="Football", kategorija="Sport", iznos=100)

