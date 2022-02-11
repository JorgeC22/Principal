from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from controlador import *
#from flask import jsonify
from flask_login import LoginManager, current_user,login_user,logout_user,login_required
from models.user import User

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



@app.route("/insertarusuario", methods = ['POST'])
def insertarusuario():
    if request.method == 'POST':
        data = request.values
        print(data)
        user_alta = insertar_usuario(request.form['username'],request.form['password'],request.form['distribuidor'],request.form.getlist('grupotrabajo[]'))
        if user_alta == True:
            flash("Registro correctamente el usuario.")
            return redirect('/altausuario')
        else:
            flash("Error: No se pudo registrar el usuario.")
            return redirect('/altausuario')


@app.route("/altausuario")
def altausuario():
    return render_template('altauser.html')

@app.route("/red")
def red():
    return render_template('red.html')


@app.route("/prueba", methods = ['POST','GET'] )
def prueba():
    if request.method == 'POST':
        userr = User(123456,'jorge','1234','myco','social')
        return render_template('consultauser.html', data = userr)
    else:
        return render_template('consultauser.html')


@app.route("/consultausuarios", methods=['GET'])
def consultausuarios():
    usuarios = obtener_usuarios()
    res = jsonify(usuarios)
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res

@app.route("/listausuarios")
def listausuarios():
    return render_template('table.html')





@app.route("/eliminarusuario", methods=['POST'])
def eliminiarusuario():
    iduser_original = verificarhash(request.form['identificador'])
    eliminar_usuario(iduser_original)
    return redirect('/listausuarios')




@app.route("/<id>/actualizarusuario")
def actualizarusuario(id):
    return render_template('actualizarusuario.html')


@app.route("/<id>/consultaactualizar", methods=['GET'])
def consultaactualizar(id):
    iduser_original = verificarhash(id)
    usuario = consulta_actualizar(iduser_original)
    res = jsonify(usuario)
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res

@app.route("/<id>/updateuser", methods = ['POST'])
def updateuser(id):
    if request.method == 'POST':
        iduser_original = verificarhash(id)
        user_update = actualizar_usuario(iduser_original,request.form['username'],request.form['distribuidor'],request.form.getlist('grupotrabajo[]'))
        if user_update == True:
            flash("Registro correctamente el usuario.")
            return redirect('/'+id+'/actualizarusuario')
        else:
            flash("Error: No se pudo registrat el usuario.")
            return redirect('/'+id+'/actualizarusuario')






@app.route("/arreglo")
def arreglo():
    flash("Error: No se pudo registrat el usuario.")
    return render_template('arreglo.html')

@app.route("/farreglo", methods = ['POST'])
def farreglo():
    arreglo = request.form.getlist('grupotrabajo[]')
    print(arreglo)
    return "hola"




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
