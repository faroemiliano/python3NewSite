from __main__ import app
from flask import Flask, request, render_template, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from modules.users.model import Usuarios
from app import db

@app.route('/registro', methods=['POST', 'GET'])
def registro():    
    if request.method == 'POST':
        usuario = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if not usuario or not email or not password:
            flash('Por favor, complete todos los campos.')
            return redirect(url_for('home'))
        print(f"Username: {usuario}, Email: {email}, Password: {password}")
    
        existing_user = Usuarios.query.filter_by(username=usuario).first()
        existing_email = Usuarios.query.filter_by(email=email).first()
    
        if existing_user or existing_email:
            flash('El usuario ya existe')
            return redirect(url_for('home'))
    
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256:600000')
        
        new_usuario = Usuarios(username=usuario, email=email, password=hashed_password)
        print(f'AQUI EL NUEVO USUARIO: {new_usuario}')
        try:
            db.session.add(new_usuario)
            db.session.commit()
        
            flash('Contacto Registrado')
            return render_template('login.html')
        except Exception as e:
            print(f'Error: {e}')
            db.session.rollback()
            flash('El usuario yaaaa existe')
            return redirect(url_for('home'))
    return render_template('usuario.html')

    
@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
        print(request.form)
        username = request.form['username']
        password = request.form['password']
        
        if not username or not password:
            flash('Por favor, complete todos los campos.')
            return redirect(url_for('login'))  # Redirige de vuelta a la página de inicio de sesión si faltan datos

        user = Usuarios.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash("Inicio de sesión exitoso!")
            return redirect(url_for('home'))  # Redirige a la página principal o a donde desees después del login
        else:
            flash("Nombre de usuario o contraseña incorrectos.")
            return redirect(url_for('login'))  # Redirige de vuelta a la página de inicio de sesión en caso de error

   return render_template('login.html') 
      