from flask import Flask, render_template, jsonify, request, redirect, url_for
from random import *
from flask_cors import CORS
from domain import Troskovi, Korisnici, Kategorije, Grupe
import requests, uuid
import os, json
from pony.orm import db_session, select
import bcrypt
import logging
from uuid import uuid4
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token


app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")

app.config['JWT_SECRET_KEY'] = 'secret'

jwt = JWTManager(app)

CORS(app)

def error(status=500, text="An error happened"):
    return jsonify({"error": text}), status

salt = bcrypt.gensalt()

def generatePass(password):
    password = password.encode('utf-8')
    hashPass = bcrypt.hashpw(password, salt).decode('utf-8')
    return hashPass


def checkPass(password, hashPass):
    print(bcrypt.checkpw(password.encode('utf-8'), hashPass.encode('utf-8')))
    return (bcrypt.checkpw(password.encode('utf-8'), hashPass.encode('utf-8')))
    #if (bcrypt.hashpw(password.encode('utf-8'), salt)) == hashPass.encode('utf-8'):
     #   return 1
    #else:
     #   return 0



@app.route('/grupa/korisnik', methods=['POST', 'DELETE'])
def dodavanje_brisanje_korisnika_grupe():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()

        email = post_data.get('email')
        ime_grupe = post_data.get('imeGrupe')
        # dodavanje po email i ime grupe
        _id = Korisnici.dodaj_korisnika_grupe(email, ime_grupe)
        print(_id)
        if _id is 0:
            response_object['message'] = 'Pogresan unos email ili ime grupe!'
        else:
            response_object['message'] = 'Korisnik dodan u grupu!'


    return jsonify(response_object)



@app.route('/korisnik/trosak', methods=['POST', 'GET'])
def ispis_korisnikove_troskove():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        email = post_data.get('email')
        data = Korisnici.dohvatiKorisnikoveTroskove(email)

        print(data)

        response_object['troskovi'] = data

    return jsonify(response_object)


@app.route('/korisnik/grupa', methods=['POST', 'GET'])
def ispis_grupa_korisnika():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()

        data = Korisnici.dohvatiGrupeKorisnika(post_data.get('email'))
        print(data)

        response_object['grupe'] = data

    return jsonify(response_object)


@app.route('/grupa', methods=['POST', 'GET'])
def dodavanje_ispis_grupe():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()

        _id = Grupe.create(post_data)

        if _id is None:
            return error()

        response_object['message'] = 'Grupa kreirana!'

    else:
        grupe = Grupe.listall()
        if grupe is None:
            return error()
        response_object['grupe'] = grupe

    return jsonify(response_object)


@app.route('/prijava', methods=['POST', 'GET'])
def prijava_korisnika():

    result = '' # {'status': 'none', 'message': 'none'}

    if request.method == 'POST':
        post_data = request.get_json()
        #if post_data is None or "id" not in post_data or id_ != post_data["id"]:
         #   return error(400, "Non-matching 'id' in body and URL")
        email = post_data.get('email')
        lozinka = post_data.get('lozinka')

        print(email)
        print(lozinka)


        res = Korisnici.prijava_korisnika(email, lozinka)


        if res is None:
            return error()

        if checkPass(lozinka, res.lozinka):
            print("checkpass")
            print(checkPass(lozinka, res.lozinka))
            access_token = create_access_token(identity = {'ime': res.ime, 'prezime': res.prezime, 'email': res.email})

            print(access_token)

            #result = access_token
            result  = {'access_token': access_token}
            result['status'] = 'success'
            result['message'] = 'Korisnik prijavljen!'

        else:
            #result = jsonify({'error': 'Invalid username and password'})
            result = {'status': 'failed'}
            result['message'] = 'Pogresno upisana email ili lozinka!'
            return error()

    return jsonify(result)
    #return jsonify(response_object)

@app.route('/korisnici', methods=['GET', 'POST'])
def svi_korisnici():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        print(post_data.get('email'))
        check = Korisnici.provjera_email(post_data.get('email'))
        if check:
            hashPass = generatePass(post_data.get('lozinka'))
            print(hashPass)

            newData= {
                "id": str(uuid4().hex),
                "ime": post_data.get('ime'),
                "prezime": post_data.get('prezime'),
                "email": post_data.get('email'),
                "lozinka": hashPass
            }

            _id = Korisnici.create(newData)


            if _id is None:
                return error()
            response_object['message'] = 'Korisnik kreiran!'
        else:
            response_object['message'] = 'Registracija nije uspjela!'
            return error()

    else:
        korisnici = Korisnici.listall()
        if korisnici is None:
            return error()
        response_object['korisnici'] = korisnici

    return jsonify(response_object)


@app.route('/troskovi/korisnik', methods=['POST', 'GET'])
def korisnikovi_troskovi():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        try:

            email = post_data.get('email')

            if email is None:
                return error()

            #Korisnici.korisnik_trosak_po_kategoriji(_email, 'Auto')

            auto = Troskovi.korisnik_trosak_po_kategoriji(email, 'Auto')
            if auto is None:
                return error()
            hrana = Troskovi.korisnik_trosak_po_kategoriji(email, 'Hrana')
            if hrana is None:
                return error()
            kuca = Troskovi.korisnik_trosak_po_kategoriji(email, 'Kuca')
            if kuca is None:
                return error()
            mobitel = Troskovi.korisnik_trosak_po_kategoriji(email, 'Mobitel')
            if mobitel is None:
                return error()
            roba = Troskovi.korisnik_trosak_po_kategoriji(email, 'Roba')
            if roba is None:
                return error()
            shop = Troskovi.korisnik_trosak_po_kategoriji(email, 'Shop')
            if shop is None:
                return error()
            sport = Troskovi.korisnik_trosak_po_kategoriji(email, 'Sport')
            if sport is None:
                return error()
            zdravlje = Troskovi.korisnik_trosak_po_kategoriji(email, 'Zdravlje')
            if zdravlje is None:
                return error()

            troskovi= {
                "auto": auto,
                "hrana": hrana,
                "kuca": kuca,
                "mobitel": mobitel,
                "roba": roba,
                "shop": shop,
                "sport": sport,
                "zdravlje": zdravlje
            }

            response_object['troskovi'] = troskovi
        except Exception as e:
            logging.exception("Error getting data")

    else:
        auto = Troskovi.dohvatiTrosakPoKategoriji('Auto')
        if auto is None:
            return error()
        hrana = Troskovi.dohvatiTrosakPoKategoriji('Hrana')
        if hrana is None:
            return error()
        kuca = Troskovi.dohvatiTrosakPoKategoriji('Kuca')
        if kuca is None:
            return error()
        mobitel = Troskovi.dohvatiTrosakPoKategoriji('Mobitel')
        if mobitel is None:
            return error()
        roba = Troskovi.dohvatiTrosakPoKategoriji('Roba')
        if roba is None:
            return error()
        shop = Troskovi.dohvatiTrosakPoKategoriji('Shop')
        if shop is None:
            return error()
        sport = Troskovi.dohvatiTrosakPoKategoriji('Sport')
        if sport is None:
            return error()
        zdravlje = Troskovi.dohvatiTrosakPoKategoriji('Zdravlje')
        if zdravlje is None:
            return error()



        troskovi= {
            "auto": auto,
            "hrana": hrana,
            "kuca": kuca,
            "mobitel": mobitel,
            "roba": roba,
            "shop": shop,
            "sport": sport,
            "zdravlje": zdravlje
        }

        response_object['troskovi'] = troskovi


    return jsonify(response_object)



@app.route('/troskovi', methods=['GET', 'POST'])
def svi_troskovi():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        _id = Korisnici.dohvatiIDpoEmailu(post_data.get('korisnik'))


        print(_id)

        newData= {
            "naziv": post_data.get('naziv'),
            "iznos": post_data.get('iznos'),
            "korisnik": _id,
            "kategorija": post_data.get('kategorija')
        }


        _i = Troskovi.create(newData)
        if _i is None:
            return error()

        response_object['message'] = 'Trosak dodan!'
    else:
        troskovi = Troskovi.listall()
        if troskovi is None:
            return error()
        response_object['troskovi'] = troskovi

    return jsonify(response_object)

@app.route('/troskovi/<trosak_id>', methods=['PUT', 'DELETE'])
def update_trosak(trosak_id):
    response_object = {'status': 'success'}

    if request.method == 'PUT':
        post_data = request.get_json()
        #if post_data is None or "id" not in post_data or id_ != post_data["id"]:
         #   return error(400, "Non-matching 'id' in body and URL")

        res = Troskovi.update(post_data)
        if res is None:
            return error()

        #izbrisi_trosak(trosak_id)
        """
        TROSKOVI.append({
            'id': uuid.uuid4().hex,
            'naziv': post_data.get('naziv'),
            'kategorija': post_data.get('kategorija'),
            'iznos': int(post_data.get('iznos'))
        })
        """
        response_object['message'] = 'Trosak izmijenjen!'

    if request.method == 'DELETE':
        #izbrisi_trosak(trosak_id)
        res = Troskovi.delete(trosak_id)
        response_object['message'] = 'Trosak izbrisan!'

    return jsonify(response_object)

def izbrisi_trosak(trosak_id):
    for t in TROSKOVI:
        if t['id'] == trosak_id:
            TROSKOVI.remove(t)
            return True
    return False


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)