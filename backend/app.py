from flask import Flask, render_template, jsonify, request, redirect, url_for
from random import *
from flask_cors import CORS
from domain import Troskovi, Korisnici
import requests, uuid
import os, json
from pony.orm import db_session, select
import bcrypt
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
    return bcrypt.checkpw(password.encode('utf-8'), hashPass.encode('utf-8'))
    #if (bcrypt.hashpw(password.encode('utf-8'), salt)) == hashPass.encode('utf-8'):
     #   return 1
    #else:
     #   return 0



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

        print(res.lozinka)

        if res is None:
            return error()

        if checkPass(lozinka, res.lozinka):
            access_token = create_access_token(identity = {'ime': res.ime, 'prezime': res.prezime, 'email': res.email})


            result = access_token
            #result['status'] = 'success'
            #result['message'] = 'Korisnik prijavljen!'

        else:
            #result = jsonify({'error': 'Invalid username and password'})
            #result['status'] = 'failed'
            #result['message'] = 'Pogresno upisana email ili lozinka!'
            return error()


    return result
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


@app.route('/troskovi', methods=['GET', 'POST'])
def svi_troskovi():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        _id = Troskovi.create(post_data)
        if _id is None:
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