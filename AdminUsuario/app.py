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





@app.route("/eliminarDistribuidorGrupotrabajo", methods=['POST'])
def eliminarDistribuidorGrupotrabajo():
    idDGT_original = verificarhashrelacion(request.form['identificador'])
    elimniar_distribuidor_grupotrabajo(idDGT_original)
    return redirect('/listausuarios')




@app.route("/<id>/actualizarRegistro")
def actualizarRegistro(id):
    return render_template('actualizarRegistro.html')


@app.route("/<id>/consultaactualizar", methods=['GET'])
def consultaactualizar(id):
    idDGT_original = verificarhashrelacion(id)
    usuario = consulta_actualizar(idDGT_original)
    res = jsonify(usuario)
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res

@app.route("/<id>/actualizarDistribuidorGrupotrabajo", methods = ['POST'])
def actualizarDistribuidorGrupotrabajo(id):
    if request.method == 'POST':
        idDGT_original = verificarhashrelacion(id)
        user_update = actualizar_distribuidor_grupotrabajo(idDGT_original,request.form['distribuidor'],request.form['grupotrabajo'])
        if user_update == True:
            flash("Registro correctamente el usuario.")
            return redirect('/'+id+'/actualizarRegistro')
        else:
            flash("Error: No se pudo registrat el usuario.")
            return redirect('/'+id+'/actualizarRegistro')




@app.route("/modificarUsuario")
def modificarUsuario():
    return render_template('modificarusuario.html')


@app.route("/actualizarUsuario", methods=['POST'])
def actualizarUsuario():
    idusuario_original = verificarhash(request.form['idusuario'])
    if idusuario_original != None:
        datajson = IDDistribuidroGrupoTrabajo(request.form.getlist('idDistribuidorGrupotrabajo[]'),request.form.getlist('distribuidor[]'),request.form.getlist('grupotrabajo[]'))
        verificacion_eliminacion_reg_distribuidor_grupotrabajo(idusuario_original,datajson)
        user_update = actualizar_usuario(idusuario_original,request.form['nombre_usuario'],datajson,request.form['ruta'])
        if user_update == True:
            flash("Registro correctamente el usuario.")
            return redirect('/modificarUsuario')
        else:
            flash("Error: No se pudo registrat el usuario.")
            return redirect('/modificarUsuario')
    flash("Error: No se pudo registrat el usuario.")
    return render_template('modificarusuario.html')

@app.route("/consultaUsuario/<nombreUsuario>", methods=['GET'])
def consultaUsuario(nombreUsuario):
    idUsuario = existencia_usuario(nombreUsuario)
    if idUsuario != None:
        usuario = consulta_usuario(idUsuario)
        res = jsonify(usuario)
        res.headers.add('Access-Control-Allow-Origin', '*')
        return res
    else:
        return "No existe Usuario"

@app.route("/eliminarUsuario", methods=['POST'])
def eliminiarUsuario():
    idUsuario_original = verificarhash(request.form['identificador'])
    if idUsuario_original != None:
        eliminarUsuario = eliminar_usuario(idUsuario_original)
        if eliminar_usuario != None:
            flash("Se Elimino Correctamente el Usuario.")
            return redirect('/modificarUsuario')
        else:
            flash("Error: No se puede eliminar el Usuario.")
            return redirect('/modificarUsuario')
    else:
        flash("Error: No se puede eliminar el Usuario.")
        return redirect('/modificarUsuario')







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
