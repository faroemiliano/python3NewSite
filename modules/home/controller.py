from __main__ import app

@app.route('/')
def home():
    return render_template('usuario.html')