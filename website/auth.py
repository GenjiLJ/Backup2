from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
import ast
from flask import request
import os
from website import response
import datetime
from flask_jwt_extended import *



auth = Blueprint('auth', __name__)

def singleObject(data):
    data = {
        'email' : data.email,
    }

    return data

@auth.route('/facerecog', methods=['GET', 'POST'])
def facerecog():
    if request.method=='POST':
        data_string = request.data.decode("UTF-8")
        data = ast.literal_eval(data_string)
        print(data)
    return{'status':True}

@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        data_string = request.data.decode("UTF-8")
        data = ast.literal_eval(data_string)
        email = data['email']
        password = data['password']

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                #flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                # return {'status':True, 'message':'Berhasil'}
                data_2 = singleObject(user)
                # futuredates = datetime.now()+timedelta(days=7)
                expires = datetime.timedelta(days=7)
                expires_refresh = datetime.timedelta(days=7)

                acces_token = create_access_token(data, fresh=True, expires_delta= expires)
                refresh_token = create_refresh_token(data, expires_delta=expires_refresh)
                return response.success({
                    "status":True,
                    "data" : data_2,
                    "access_token" : acces_token,
                    "refresh_token" : refresh_token,
                }, "Sukses Login!")
            else:
                #flash('Incorrect password, try again.', category='error')
                return {'status':False, 'message':'Incorrect password, try again.' }
        else:
            #flash('Email does not exist.', category='error')
            return {'status':False, 'message':'Email does not exist.'}

    return {'status':False, 'message':''}


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        try:
            data_string = request.data.decode("UTF-8")
            data = ast.literal_eval(data_string)
            image = data['image']
            email = data['email']
            password1 = data['password1']
            password2 = data['password2']
            if image != data[''] and email != data[''] and password1 != data[''] and password2 != data['']:
            # while image == data[''] or email == data[''] or password1 ==data[''] or password2 ==data[''] :
            #     wait
                try:
                    user = User.query.filter_by(email=email).first()
                    if user:
                        #flash('Email already exists.', category='error')
                        return {'status':False, 'message':'Email already exists.'}
                    elif len(email) < 4:
                        #flash('Email must be greater than 3 characters.', category='error')
                        return {'status':False, 'message':'Email must be greater than 3 characters.'}
                    # elif len(nama) < 3:
                    #     #flash('NIK must be greater than 16.', category='error')
                    #     return {'status':False, 'message':'Name must be greater than 3 characters'}
                    elif password1 != password2:
                        #flash('Passwords don\'t match.', category='error')
                        return {'status':False, 'message':'Password Dont match.'}
                    elif len(password1) < 7:
                        #flash('Password must be at least 7 characters.', category='error')
                        return {'status':False, 'message':'Password Dont match.'}
                    elif len (image) != 0 :
                        return {'status': False, 'message':'Capture image first' }
                    else:
                        new_user = User(email=email,image=image, password=generate_password_hash(
                            password1, method='sha256'))
                        db.session.add(new_user)
                        db.session.commit()
                        login_user(new_user, remember=True)
                        #flash('Account created!', category='success')
                        return {'status':True, 'message':'Account Created'}
                except:
                    return{'message':'lengkapi data'}
        except:
            return{'message': 'Email dan password belum di isi '}
        

    return {'status':False, 'message':''}
