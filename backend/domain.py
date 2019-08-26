from pony.orm import db_session, select
import logging
from model import Trosak, Korisnik
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


class Troskovi(Base):
    model_class = Trosak


class Korisnici(Base):
    model_class = Korisnik

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




