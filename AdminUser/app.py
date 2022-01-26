from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from controlador import mostrar, loggin_user, loader_user, up_user
#from flask import jsonify
from flask_login import LoginManager, current_user,login_user,logout_user,login_required

app = Flask(__name__, template_folder='templates')
app.secret_key = 'dont tell anyone'
login_manager_app=LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return loader_user(id)


@app.route("/")
def inicio():
    #flash('Mensaje de prueba!')
    return render_template('login.html')







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



@app.route("/userup", methods = ['POST'])
def userup():
    if request.method == 'POST':
        user_alta = up_user(request.form['username'],request.form['password'],request.form['distribuidor'],request.form['grupotrabajo'])
        if user_alta == True:
            flash("Registro correctamente el usuario.")
            return redirect('/altausuario')
        else:
            flash("Error: No se pudo registrat el usuario.")
            return redirect('/altausuario')

@app.route("/altausuario")
def altausuario():
    return render_template('altauser.html')










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
