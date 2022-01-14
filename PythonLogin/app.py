from flask import Flask, render_template, request, redirect, url_for, flash
from controlador import mostrar, login_user
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template('table.html')

@app.route("/read/<empresa>")
def read(empresa):
    data = mostrar(empresa)
    #lef = jsonify(data)
    #data = {"name": "jorge","edad": 22}
    #return render_template('table.html', dpeliculas=lef)
    return data


@app.route("/login", methods = ['POST'])
def login():
    if request.method == 'POST':
        firma = login_user(request.form['correo'],request.form['pssd'])
        if firma['bandera'] == "true":
            return redirect('/read/'+firma['empresa'] )
        else:
            #flash("Mensaje de prueba")
            return "Error: El correo o contraseña son erroneos."
            #return redirect(url_for('inicio'))
            #return render_template('/', error=mess)


if __name__== "__main__":
    app.run()
