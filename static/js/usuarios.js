window.onload=function(){
    usuarios();
    function usuarios(){
        var xhttp = new XMLHttpRequest();
        xhttp.open('GET','http://127.0.0.1:5000/consultausuarios', true);
        xhttp.send();
        xhttp.onreadystatechange = function(){
            if(this.readyState==4 && this.status==200){
                var json = JSON.parse(this.responseText);
                console.log(json);
                

                var encabezado = ['Nombre usuario','Distribuidor','Grupo de trabajo','Editar','Eliminar'];

                for(var i of encabezado){
                    var columna = document.createElement("th");
                    columna.setAttribute("scope","col")
                    var texto = document.createTextNode(i);
                    columna.appendChild(texto);
                    document.getElementById("encabezado").appendChild(columna);
                }

                for(var i=0;i<json.length;i++){
                    var renglon = document.createElement("tr");
                    renglon.setAttribute("id",json[i].id+'_'+i)
                    document.getElementById("res").appendChild(renglon);

                    var celda = document.createElement("td");
                    var texto = document.createTextNode(json[i].nombre_usuario);
                    celda.appendChild(texto);
                    document.getElementById(json[i].id+'_'+i).appendChild(celda);

                    var celda = document.createElement("td");
                    var texto = document.createTextNode(json[i].distribuidor);
                    celda.appendChild(texto);
                    document.getElementById(json[i].id+'_'+i).appendChild(celda);

                    var celda = document.createElement("td");
                    var texto = document.createTextNode(json[i].grupo_trabajo);
                    celda.appendChild(texto);
                    document.getElementById(json[i].id+'_'+i).appendChild(celda);

                    var celda = document.createElement("td");
                    var btn = document.createElement("button");
                    btn.setAttribute("type","button");
                    btn.setAttribute("class","btn btn-sm btn-outline-secondary");
                    btn.setAttribute("id","editar"+json[i].id);
                    btn.setAttribute("onclick","location.href='http://127.0.0.1:5000/"+json[i].id+"/actualizarusuario';")
                    celda.appendChild(btn);
                    var texto = document.createTextNode("Editar");
                    btn.appendChild(texto);
                    document.getElementById(json[i].id+'_'+i).appendChild(celda);

                    var celda = document.createElement("td");
                    var form = document.createElement("form");
                    form.setAttribute('action', 'http://127.0.0.1:5000/eliminarusuario');
                    form.setAttribute('method', 'POST');
                    celda.appendChild(form);
                    var btn = document.createElement("button");
                    btn.setAttribute("class","btn btn-sm btn-outline-secondary");
                    btn.setAttribute('name', 'identificador');
                    btn.setAttribute('value', json[i].id)
                    form.appendChild(btn);
                    var texto = document.createTextNode("Eliminar");
                    btn.appendChild(texto);
                    document.getElementById(json[i].id+'_'+i).appendChild(celda);
                }

                document.getElementById("editar1").addEventListener("click", editarUsuario)

                function editarUsuario(){
                    var title = document.createElement("h1");
                    title.setAttribute("class","h3");
                    title.setAttribute("id","texto");
                    var texto = document.createTextNode("Editar");
                    title.appendChild(texto);
                    document.getElementById("columna").appendChild(title);

                    var form = document.createElement("form");
                    form.setAttribute("action","{{url_for('actualizarUsuario')}}");
                    form.setAttribute("method","post");
                    form.setAttribute("id","actualizar")
                    document.getElementById("columna").appendChild(form);

                    var id = document.createElement("input");
                    id.setAttribute("type","hidden");
                    id.setAttribute("name","id");
                    id.setAttribute("value","{{"+json[i].id+"}}");
                    document.getElementById("actualizar").appendChild(id);

                    var label = document.createElement("label");
                    label.setAttribute("for","nombre");
                    var texto = document.createTextNode("Nombre:")
                    label.appendChild(texto);
                    document.getElementById("actualizar").appendChild(label);

                    var nombre = document.createElement("input");
                    nombre.setAttribute("value",json[i].username);
                    nombre.setAttribute("type","text");
                    nombre.setAttribute("class","form-control");
                    nombre.setAttribute("placeholder","Nombre");
                    nombre.setAttribute("name","nombre");
                    nombre.setAttribute("id","nombre");
                    document.getElementById("actualizar").appendChild(nombre);

                    var label = document.createElement("label");
                    label.setAttribute("for","contraseña");
                    label.setAttribute("class","mt-2")
                    var texto = document.createTextNode("Contraseña:")
                    label.appendChild(texto);
                    document.getElementById("actualizar").appendChild(label);

                    var contraseña = document.createElement("input");
                    contraseña.setAttribute("value",json[i].distribuidor);
                    contraseña.setAttribute("type","text");
                    contraseña.setAttribute("class","form-control");
                    contraseña.setAttribute("placeholder","Contraseña");
                    contraseña.setAttribute("name","contraseña");
                    contraseña.setAttribute("id","nombre");
                    document.getElementById("actualizar").appendChild(contraseña);

                    var guardar = document.createElement("button");
                    guardar.setAttribute("type","submit");
                    guardar.setAttribute("class","btn btn-sm btn-outline-secondary mt-2");
                    var texto = document.createTextNode("Guardar");
                    guardar.appendChild(texto);
                    document.getElementById("actualizar").appendChild(guardar);

                    var limpiar = document.createElement("button");
                    limpiar.setAttribute("class","btn btn-sm btn-outline-secondary mt-2 ms-2");
                    limpiar.setAttribute("id","limpiar")
                    var texto = document.createTextNode("Limpiar");
                    limpiar.appendChild(texto);
                    document.getElementById("actualizar").appendChild(limpiar);

                    document.getElementById("limpiar").addEventListener("click",borrar)
                    function borrar(){
                        var elemento=document.getElementById("columna");
		                while(elemento.firstChild){
			                elemento.removeChild(elemento.firstChild);
		                }
                    }
                }
            }
        };
    }
}



