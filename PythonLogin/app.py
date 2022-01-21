from flask import Flask, render_template, request, redirect, url_for, flash
from controlador import mostrar, loggin_user, loader_user
#from flask import jsonify
from flask_login import LoginManager, current_user,login_user,logout_user,login_required

app = Flask(__name__)
app.secret_key = 'dont tell anyone'
login_manager_app=LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return loader_user(id)


@app.route("/")
def inicio():
    #flash('Mensaje de prueba!')
    return render_template('login.html')

@app.route("/<distribuidor>/home")
@login_required
def home(distribuidor):
    #data = mostrar(empresa)
    #lef = jsonify(data)
    #data = {"name": "jorge","edad": 22}
    #return render_template('table.html', pelis=data)
    #return data
    return render_template('home.html')

@app.route("/<distribuidor>/home/abonos")
def abonos(distribuidor):
    if current_user.is_authenticated:
        #return current_user.distribuidor
        return distribuidor
    else:
        return redirect('/')


@app.route("/<distribuidor>/home/comision")
def comision(distribuidor):
    if current_user.is_authenticated:
        return distribuidor
    else:
        return redirect('/')



"""@app.route("/home/extension")
def extension():
    if current_user.is_authenticated:
        return current_user.distribuidor
    else:
        return "no autenticado"""


@app.route("/login", methods = ['POST'])
def login():
    if request.method == 'POST':
        logger_user = loggin_user(request.form['correo'],request.form['password'])
        if logger_user != None:
            login_user(logger_user)
            return redirect('/'+logger_user.distribuidor+'/home')
        else:
            flash("Error: El correo o contraseña son erroneos")
            return redirect('/')

@app.route("/logout")
def logout():
    logout_user()
    return redirect('/')


@app.errorhandler(401)
def status_401(error):
    return redirect('/')

@app.errorhandler(404)
def status_404(error):
    return "<h1>Pagina no encontrada</h1>", 404

if __name__== "__main__":
    #app.register_error_handler(401, status_401)
    #app.register_error_handler(404, status_404)
    app.run(debug=True)
