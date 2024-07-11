from __main__ import app
from flask import Flask, render_template 

@app.route('/productos')
def productos():
    return render_template('productosInicial.html') 