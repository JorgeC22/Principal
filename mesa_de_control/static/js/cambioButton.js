window.onload=function(){
    usuarios();
    function usuarios(){
        var URLactual = document.URL;
        var URLnew = URLactual.replace("pagina2", "consultaVariables");
        console.log(URLnew);

        var xhttp = new XMLHttpRequest();
        xhttp.open('GET',URLnew, true);
        xhttp.send();
        xhttp.onreadystatechange = function(){
            if(this.readyState==4 && this.status==200){
                var json = JSON.parse(this.responseText);
                
                var form_aceptarVariables = document.getElementById('form_aceptarVariables');
                form_aceptarVariables.setAttribute('action', URLnew);

                var inputIDinstanciaP = document.getElementById('idproceso');
                inputIDinstanciaP.setAttribute('value', json.idproceso);

                var inputNombre = document.getElementById('nombre');
                inputNombre.value = json.nombre;

                var inputPaterno = document.getElementById('apellidoP');
                inputPaterno.value = json.paterno;
                var inputMaterno = document.getElementById('apellidoM');
                inputMaterno.value = json.materno;
                var inputEmpresa = document.getElementById('empresa');
                inputEmpresa.value = json.empresa;

                //var inputTarea = document.getElementById('actividad');

                console.log(json.tarea)
                if (json.tarea == "Verificar Datos"){
                    
                    //var varEjemplo = boton(texto,formaction,name,value,class,id);
                    var btnAceptar = boton("Aceptar Variables","/acceso","verificar","True","btn btn-success","btnAceptarVar");
                    var btnRechazar = boton("Rechazar","/acceso2","verificar","False","btn btn-danger","btnRechazarVar");

                    //form_aceptarVariables.appendChild(btnAceptar);
                    form_aceptarVariables.appendChild(btnAceptar);
                    form_aceptarVariables.appendChild(btnRechazar);
                } 
                if (json.tarea == "Realizar Contrato"){
                    
                    var btnAceptar = boton("Enviar Contrato","/acceso","verificar","True","btn btn-success","btnAceptarVar");
                    var btnRechazar = boton("Rechazar Contrato","/acceso2","verificar","False","btn btn-danger","btnRechazarVar");

                    form_aceptarVariables.appendChild(btnAceptar);
                    form_aceptarVariables.appendChild(btnRechazar);
                }
            }
            
        };
    }
}

//Funcion para la creacion de botones submit.
function boton(texto,formaction,name,value,clase,id){
    var btnAceptar = document.createElement("button");
    btnAceptar.setAttribute('type', 'submit');
    btnAceptar.setAttribute('id', id);
    btnAceptar.setAttribute('class', clase);
    btnAceptar.setAttribute('formaction', formaction)
    btnAceptar.setAttribute('name', name),
    btnAceptar.setAttribute('value', value)
    var textoBtn = document.createTextNode(texto);
    btnAceptar.appendChild(textoBtn);
    return btnAceptar
};