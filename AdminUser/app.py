from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from controlador import *

app = Flask(__name__, template_folder='templates')
app.secret_key = 'dont tell anyone'





@app.route("/insertarusuario", methods = ['POST'])
def insertarusuario():
    if request.method == 'POST':
        arrayDistribuidorGrupoTrabajo = relacionDistribuidroGrupoTrabajo(request.form.getlist('distribuidor[]'),request.form.getlist('grupotrabajo[]'))
        print(arrayDistribuidorGrupoTrabajo)
        user_alta = insertar_usuario(request.form['username'],request.form['password'],arrayDistribuidorGrupoTrabajo)
        if user_alta == True:
            flash("Registro correctamente el usuario.")
            return redirect('/altausuario')
        else:
            flash("Error: No se pudo registrar el usuario.")
            return redirect('/altausuario')


@app.route("/altausuario")
def altausuario():
    return render_template('altauser.html')





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
    idDGT_original = verificarhashrelacion(request.form['identificador'])
    elimniar_distribuidor_grupotrabajo(idDGT_original)
    return redirect('/listausuarios')




@app.route("/<id>/actualizarusuario")
def actualizarusuario(id):
    return render_template('actualizarusuario.html')


@app.route("/<id>/consultaactualizar", methods=['GET'])
def consultaactualizar(id):
    idDGT_original = verificarhashrelacion(id)
    usuario = consulta_actualizar(idDGT_original)
    res = jsonify(usuario)
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res

@app.route("/<id>/updateuser", methods = ['POST'])
def updateuser(id):
    if request.method == 'POST':
        idDGT_original = verificarhashrelacion(id)
        user_update = actualizar_usuario(idDGT_original,request.form['distribuidor'],request.form['grupotrabajo'])
        if user_update == True:
            flash("Registro correctamente el usuario.")
            return redirect('/'+id+'/actualizarusuario')
        else:
            flash("Error: No se pudo registrat el usuario.")
            return redirect('/'+id+'/actualizarusuario')





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
