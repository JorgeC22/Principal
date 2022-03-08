from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from controlador import *

app = Flask(__name__, template_folder='templates')
app.secret_key = 'dont tell anyone'

@app.route('/<ruta>')
def login(ruta):
    ruta_usuario = existeRuta(ruta)
    if ruta_usuario != None:
        rol = isAdmin(ruta_usuario['id_usuario'])
        if rol != None:
            return render_template('table.html')
        else:
            return render_template('home.html')
    else:
        return redirect('/')

@app.route('/<ruta>/<tipo_movimiento>/<anio>', methods=['GET'])
def movimientos(ruta,tipo_movimiento,anio):
    nombreDistribuidor = obtieneDistribuidor(ruta)
    if nombreDistribuidor != None:
        distribuidor = nombreDistribuidor['distribuidor']
        #Llamamos a cada funcion y retornamos la data
        res = obtieneMovimientos(distribuidor,tipo_movimiento,anio)
        data = creacionJSON(res)
        dic = agruparMovimientos(res, data)
        response = jsonify(dic)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        return redirect('/')





@app.route("/<ruta>/insertarusuario", methods = ['POST'])
def insertarusuario(ruta):
    if request.method == 'POST':
        arrayDistribuidorGrupoTrabajo = relacionDistribuidroGrupoTrabajo(request.form.getlist('distribuidor[]'),request.form.getlist('grupotrabajo[]'))
        print(arrayDistribuidorGrupoTrabajo)
        user_alta = insertar_usuario(request.form['username'],request.form['password'],arrayDistribuidorGrupoTrabajo)
        if user_alta == True:
            flash("Registro correctamente el usuario.")
            return redirect('/'+ruta+'/altausuario')
        else:
            flash("Error: No se pudo registrar el usuario.")
            return redirect('/'+ruta+'/altausuario')


@app.route("/<ruta>/altausuario")
def altausuario(ruta):
    user = rutaAdmin(ruta)
    if user['tipo_rol'] == 'admin':
        return render_template('altauser.html')
    else:
        return redirect('/')





@app.route("/<ruta>/consultausuarios", methods=['GET'])
def consultausuarios(ruta):
    user = rutaAdmin(ruta)
    if user['tipo_rol'] == 'admin':
        usuarios = obtener_usuarios()
        res = jsonify(usuarios)
        res.headers.add('Access-Control-Allow-Origin', '*')
        return res
    else:
        return redirect('/')

@app.route("/<ruta>/eliminarDistribuidorGrupotrabajo", methods=['POST'])
def eliminarDistribuidorGrupotrabajo(ruta):
    user = rutaAdmin(ruta)
    if user['tipo_rol'] == 'admin':
        idDGT_original = verificarhashrelacion(request.form['identificador'])
        elimniar_distribuidor_grupotrabajo(idDGT_original)
        return redirect('/'+ruta+'')
    else:
        return redirect('/')



@app.route("/<ruta>/<id>/actualizarRegistro")
def actualizarRegistro(ruta,id):
    user = rutaAdmin(ruta)
    if user['tipo_rol'] == 'admin':
        return render_template('actualizarRegistro.html')
    else:
        return redirect('/')


@app.route("/<ruta>/<id>/consultaactualizar", methods=['GET'])
def consultaactualizar(ruta,id):
    user = rutaAdmin(ruta)
    if user['tipo_rol'] == 'admin':
        idDGT_original = verificarhashrelacion(id)
        usuario = consulta_actualizar(idDGT_original)
        res = jsonify(usuario)
        res.headers.add('Access-Control-Allow-Origin', '*')
        return res
    else:
        return redirect('/')

@app.route("/<ruta>/<id>/actualizarDistribuidorGrupotrabajo", methods = ['POST'])
def actualizarDistribuidorGrupotrabajo(ruta,id):
    user = rutaAdmin(ruta)
    if user['tipo_rol'] == 'admin':
        if request.method == 'POST':
            idDGT_original = verificarhashrelacion(id)
            user_update = actualizar_distribuidor_grupotrabajo(idDGT_original,request.form['distribuidor'],request.form['grupotrabajo'])
            if user_update == True:
                flash("Actualizo correctamente el usuario.")
                return redirect('/'+ruta+'/'+id+'/actualizarRegistro')
            else:
                flash("Error: No se pudo actualizar el usuario.")
                return redirect('/'+ruta+'/'+id+'/actualizarRegistro')
    else:
        return redirect('/')




@app.route("/<ruta>/modificarUsuario")
def modificarUsuario(ruta):
    user = rutaAdmin(ruta)
    if user['tipo_rol'] == 'admin':
        return render_template('modificarusuario.html')
    else:
        return redirect('/')


@app.route("/<ruta>/actualizarUsuario", methods=['POST'])
def actualizarUsuario(ruta):
    user = rutaAdmin(ruta)
    if user['tipo_rol'] == 'admin':
        idusuario_original = verificarhash(request.form['idusuario'])
        if idusuario_original != None:
            datajson = IDDistribuidroGrupoTrabajo(request.form.getlist('idDistribuidorGrupotrabajo[]'),request.form.getlist('distribuidor[]'),request.form.getlist('grupotrabajo[]'))
            verificacion_eliminacion_reg_distribuidor_grupotrabajo(idusuario_original,datajson)
            user_update = actualizar_usuario(idusuario_original,request.form['nombre_usuario'],datajson,request.form['ruta'])
            if user_update == True:
                flash("Actualizo correctamente el usuario.")
                return redirect('/'+ruta+'/modificarUsuario')
            else:
                flash("Error: No se pudo actualizar el usuario.")
                return redirect('/'+ruta+'/modificarUsuario')
        flash("Error: No existe el usuario.")
        return render_template('modificarusuario.html')
    else:
        return redirect('/')

@app.route("/<ruta>/consultaUsuario/<nombreUsuario>", methods=['GET'])
def consultaUsuario(ruta,nombreUsuario):
    user = rutaAdmin(ruta)
    if user['tipo_rol'] == 'admin':
        idUsuario = existencia_usuario(nombreUsuario)
        if idUsuario != None:
            usuario = consulta_usuario(idUsuario)
            res = jsonify(usuario)
            res.headers.add('Access-Control-Allow-Origin', '*')
            return res
        else:
            jsonError = [{"status": "false", "description": "No se encontro el usuario especificado."}]
            res = jsonify(jsonError)
            res.headers.add('Access-Control-Allow-Origin', '*')
            return res
    else:
        return redirect('/')

@app.route("/<ruta>/eliminarUsuario", methods=['POST'])
def eliminiarUsuario(ruta):
    user = rutaAdmin(ruta)
    if user['tipo_rol'] == 'admin':
        idUsuario_original = verificarhash(request.form['identificador'])
        if idUsuario_original != None:
            eliminarUsuario = eliminar_usuario(idUsuario_original)
            if eliminar_usuario != None:
                flash("Se Elimino Correctamente el Usuario.")
                return redirect('/'+ruta+'/modificarUsuario')
            else:
                flash("Error: No se puede eliminar el Usuario.")
                return redirect('/'+ruta+'/modificarUsuario')
        else:
            flash("Error: No se puede eliminar el Usuario.")
            return redirect('/'+ruta+'/modificarUsuario')
    else:
        return redirect('/')







@app.errorhandler(401)
def status_401(error):
    return redirect('/')


@app.errorhandler(404)
def status_404(error):
    return render_template('privacidad.html'), 404

if __name__== "__main__":
    #app.register_error_handler(401, status_401)
    #app.register_error_handler(404, status_404)
    app.run(debug=True)
