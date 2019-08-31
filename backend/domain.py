from pony.orm import db_session, select
import logging
from model import Trosak, Korisnik, Kategorija, Grupa
import datetime as dt
from collections import deque
from decimal import Decimal
import bcrypt


class Base:
    @classmethod
    @db_session()
    def get(cls, id_):
        try:
            unit = cls.model_class[id_]
            return unit.to_dict()
        except Exception as e:
            logging.exception("Error getting by id")

    @classmethod
    @db_session()
    def delete(cls, id_):
        try:
            cls.model_class[id_].delete()
            return True
        except Exception as e:
            logging.exception("Error deleting data")

    @classmethod
    @db_session()
    def create(cls, data):
        try:
            unit = cls.model_class(**data)
            return unit.id
        except Exception as e:
            logging.exception("Error saving data")

    @classmethod
    @db_session()
    def update(cls, data):
        try:
            unit = cls.model_class[data["id"]]
            unit.set(**data)
            return True
        except Exception as e:
            logging.exception("Error saving data")

    @classmethod
    @db_session()
    def listall(cls):
        try:
            units = select(u for u in cls.model_class)
            return [u.to_dict() for u in units]
        except Exception as e:
            logging.exception("Error saving data")


class Kategorije(Base):
    model_class = Kategorija

class Grupe(Base):
    model_class = Grupa



class Troskovi(Base):
    model_class = Trosak

    @classmethod
    @db_session
    def dohvatiTrosakPoKategoriji(cls, _naziv):

        data = select(sum(t.iznos) for t in Trosak if t.kategorija.naziv == _naziv)

        if data is None:
            return None

        return data.first()


    @classmethod
    @db_session
    def korisnik_trosak_po_kategoriji(cls, _email, _naziv):

        data = select(sum(t.iznos) for t in Trosak if t.kategorija.naziv == _naziv and t.korisnik.email == _email)

        if data is None:
            return None

        return data.first()




class Korisnici(Base):
    model_class = Korisnik

    @classmethod
    @db_session
    def troskovi_korisnika_po_kategoriji(cls, _email,  _kategorija):

        k = Korisnik.get(email = _email)
        troskovi = k.trosak

        data = select(t for t in troskovi if t.kategorija.naziv == _kategorija)

        return [u.to_dict() for u in data]

    @classmethod
    @db_session
    def dohvatiKorisnikoveTroskove(cls, _email):

        k = Korisnik.get(email = _email)
        data = k.trosak.copy()

        if data is None:
            return None

        return [d.to_dict() for d in data]

    @classmethod
    @db_session
    def dohvatiGrupeKorisnika(cls, _email):

        k = Korisnik.get(email = _email)
        data = k.grupa.copy()

        if data is None:
            return None

        return [d.to_dict() for d in data]

    @classmethod
    @db_session
    def dohvatiIDpoEmailu(cls, _email):
        kor = Korisnik.get(email = _email)
        return kor.id


    @classmethod
    @db_session
    def dodaj_korisnika_grupe(cls, _email, _ime):

        kor = Korisnik.get(email = _email)
        print(kor)

        if kor is None:
            return 0

        gru = Grupa.get(ime = _ime)

        print(gru)

        if gru is None:
            return 0

        test = kor.grupa.add(gru)

        print(test)
        return 1

        #if test is None:
         #   return 0
        #else:
         #   return 1



    @classmethod
    @db_session
    def provjera_email(cls, _email):
        try:
            provjera = Korisnik.get(email = _email)
            if provjera == None:
                return 1
            else:
                return 0
        except Exception as e:
            logging.exception("Error getting by email")

    @classmethod
    @db_session
    def prijava_korisnika(cls, _email, _lozinka):
        try:
            kor = Korisnik.get(email = _email)
            if kor != None:
                return kor
            else:
                return None
               # if bcrypt.checkpw(_lozinka.encode('utf-8'), kor.lozinka.encode('utf-8')):
                #    return 1
                #else:
                 #   return 0

            #provjera = Korisnik.get(email = _email, lozinka = _lozinka)
            #if provjera != None:
            #    return 1
            #else:
             #   return 0
        except Exception as e:
            logging.exception("Error getting by email")




