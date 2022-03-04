window.onload=function(){
    usuarios();
    function usuarios(){
        var xhttp = new XMLHttpRequest();
        xhttp.open('GET','http://127.0.0.1:5000/consultausuarios', true);
        xhttp.send();
        xhttp.onreadystatechange = function(){
            if(this.readyState==4 && this.status==200){
                var json = JSON.parse(this.responseText);
                
                

                var encabezado = ['Nombre de Usuario','Contraseña','Distribuidor','Grupo de Trabajo','Ruta','Editar','Eliminar'];

                for(var i of encabezado){
                    var columna = document.createElement("th");
                    columna.setAttribute("scope","col")
                    var texto = document.createTextNode(i);
                    columna.appendChild(texto);
                    document.getElementById("encabezado").appendChild(columna);
                }

                for(var i=0;i<json.length;i++){
                    var renglon = document.createElement("tr");
                    renglon.setAttribute("id",json[i].id_usuario+'_'+i)
                    document.getElementById("res").appendChild(renglon);

                    var celda = document.createElement("td");
                    var texto = document.createTextNode(json[i].nombre_usuario);
                    celda.appendChild(texto);
                    document.getElementById(json[i].id_usuario+'_'+i).appendChild(celda);

                    var celda = document.createElement("td");
                    var texto = document.createTextNode(json[i].contraseña);
                    celda.appendChild(texto);
                    document.getElementById(json[i].id_usuario+'_'+i).appendChild(celda);

                    var celda = document.createElement("td");
                    var texto = document.createTextNode(json[i].distribuidor);
                    celda.appendChild(texto);
                    document.getElementById(json[i].id_usuario+'_'+i).appendChild(celda);

                    var celda = document.createElement("td");
                    var texto = document.createTextNode(json[i].grupotrabajo);
                    celda.appendChild(texto);
                    document.getElementById(json[i].id_usuario+'_'+i).appendChild(celda);

                    var celda = document.createElement("td");
                    var texto = document.createTextNode(json[i].ruta);
                    celda.appendChild(texto);
                    document.getElementById(json[i].id_usuario+'_'+i).appendChild(celda);

                    /*var celda = document.createElement("td");
                    var btn = document.createElement("button");
                    btn.setAttribute("type","button");
                    btn.setAttribute("class","btn btn-sm btn-outline-secondary");
                    btn.setAttribute("href","{{url_for('movimientoUsuario', nombre="+i[1]+")}}");
                    celda.appendChild(btn);
                    var texto = document.createTextNode("Obtener");
                    btn.appendChild(texto);
                    document.getElementById(items[0]).appendChild(celda);*/

                    //Celda de Boton para Editar
                    var celda = document.createElement("td");
                    var btn = document.createElement("button");
                    btn.setAttribute("type","button");
                    btn.setAttribute("class","btn btn-sm btn-outline-secondary");
                    btn.setAttribute("id","editar"+json[i].id_usuario);
                    btn.setAttribute("onclick","location.href='http://127.0.0.1:5000/"+json[i].id_distribuidor_grupotrabajo+"/actualizarRegistro';")
                    celda.appendChild(btn);
                    var texto = document.createTextNode("Editar");
                    btn.appendChild(texto);
                    document.getElementById(json[i].id_usuario+'_'+i).appendChild(celda);
                    
                    //Celda de Boton para eliminar
                    var celda = document.createElement("td");
                    var form = document.createElement("form");
                    form.setAttribute('action', 'http://127.0.0.1:5000/eliminarDistribuidorGrupotrabajo');
                    form.setAttribute('method', 'POST');
                    celda.appendChild(form);
                    var btn = document.createElement("button");
                    btn.setAttribute("class","btn btn-sm btn-outline-secondary");
                    btn.setAttribute('name', 'identificador');
                    btn.setAttribute('value', json[i].id_distribuidor_grupotrabajo)
                    form.appendChild(btn);
                    var texto = document.createTextNode("Eliminar");
                    btn.appendChild(texto);
                    document.getElementById(json[i].id_usuario+'_'+i).appendChild(celda);
                }
            }
        };
    }
}



