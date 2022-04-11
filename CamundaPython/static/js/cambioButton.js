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
                    
                    var btnAceptar = document.createElement("button");
                    btnAceptar.setAttribute('type', 'submit');
                    btnAceptar.setAttribute('id', 'btnAceptar');
                    btnAceptar.setAttribute('class', 'btn btn-success');
                    btnAceptar.setAttribute('formaction', '/acceso')
                    btnAceptar.setAttribute('name', 'verificar'),
                    btnAceptar.setAttribute('value', 'True')
                    var texto = document.createTextNode("Aceptar Variables");
                    btnAceptar.appendChild(texto);

                    var btnRechazar = document.createElement("button");
                    btnRechazar.setAttribute('type', 'submit');
                    btnRechazar.setAttribute('id', 'btnAceptar');
                    btnRechazar.setAttribute('class', 'btn btn-danger');
                    btnRechazar.setAttribute('formaction', '/acceso2')
                    btnRechazar.setAttribute('name', 'verificar'),
                    btnRechazar.setAttribute('value', 'False')
                    var texto = document.createTextNode("Rechazar");
                    btnRechazar.appendChild(texto);


                    form_aceptarVariables.appendChild(btnAceptar);
                    form_aceptarVariables.appendChild(btnRechazar);
                } 
                if (json.tarea == "Contrato Personal"){
                    
                    var btnAceptar = document.createElement("button");
                    btnAceptar.setAttribute('type', 'submit');
                    btnAceptar.setAttribute('id', 'btnAceptar');
                    btnAceptar.setAttribute('class', 'btn btn-success');
                    btnAceptar.setAttribute('formaction', '/acceso')
                    btnAceptar.setAttribute('name', 'verificar'),
                    btnAceptar.setAttribute('value', 'True')
                    var texto = document.createTextNode("Enviar Contrato");
                    btnAceptar.appendChild(texto);

                    var btnRechazar = document.createElement("button");
                    btnRechazar.setAttribute('type', 'submit');
                    btnRechazar.setAttribute('id', 'btnAceptar');
                    btnRechazar.setAttribute('class', 'btn btn-danger');
                    btnRechazar.setAttribute('formaction', '/acceso2')
                    btnRechazar.setAttribute('name', 'verificar'),
                    btnRechazar.setAttribute('value', 'False')
                    var texto = document.createTextNode("Rechazar Contrato");
                    btnRechazar.appendChild(texto);

                    form_aceptarVariables.appendChild(btnAceptar);
                    form_aceptarVariables.appendChild(btnRechazar);
                }
            }
            
        };
    }
}