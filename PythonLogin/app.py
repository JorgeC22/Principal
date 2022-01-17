from flask import Flask, render_template, request, redirect, url_for, flash
from controlador import mostrar, login_user
from flask import jsonify

app = Flask(__name__)
app.secret_key = 'dont tell anyone'


@app.route("/")
def inicio():
    #flash('Mensaje de prueba!')
    return render_template('login.html')

@app.route("/info/<empresa>")
def info(empresa):
    data = mostrar(empresa)
    #lef = jsonify(data)
    #data = {"name": "jorge","edad": 22}
    return render_template('table.html', pelis=data)
    #return data

@app.route("/login", methods = ['POST'])
def login():
    if request.method == 'POST':
        credenciales = login_user(request.form['correo'],request.form['password'])
        if credenciales['acceso'] == "true":
            return redirect('/info/'+credenciales['empresa'] )
        else:
            flash("Error: El correo o contraseña son erroneos")
            return redirect('/')


if __name__== "__main__":
    app.run()
