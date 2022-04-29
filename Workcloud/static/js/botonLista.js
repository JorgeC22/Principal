window.onload=function(){
    usuarios();
    function usuarios(){
        var URLactual = document.URL;
        var URLnew = URLactual.replace("listaVerificarDatos", "consultaInstancias");
        console.log(URLnew);

        var xhttp = new XMLHttpRequest();
        xhttp.open('GET',URLnew, true);
        xhttp.send();
        xhttp.onreadystatechange = function(){
            if(this.readyState==4 && this.status==200){
                var json = JSON.parse(this.responseText);
                
                var form_aceptarVariables = document.getElementById('form_aceptarVariables');
                form_aceptarVariables.setAttribute('action', URLnew);

                var table_body = document.getElementById('table_body');

                for (let i = 0; i < json.length; i++) {
                    
                    var renglon = document.createElement("tr");

                    var idProceso = document.createElement("td");
                    var textoCampo = document.createTextNode(json[i].idproceso);
                    idProceso.appendChild(textoCampo);

                    var tarea = document.createElement("td");
                    var textoCampo = document.createTextNode(json[i].tarea);
                    tarea.appendChild(textoCampo);

                    var btn = document.createElement("td");
                    var btnInstancia = boton("Abrir Instancia","","btn btn-success","abrirInstancia");
                    btn.appendChild(btnInstancia);

                    console.log(json.tarea)
                    //if (json.tarea == "Carga documentación de razón social"){
                        //var varEjemplo = boton(texto,name,class,id);
                        
                    //}

                    renglon.appendChild(idProceso);
                    renglon.appendChild(tarea);
                    renglon.appendChild(btn);
                    table_body.appendChild(renglon);
                }
            }
        }
    }
}

//Funcion para la creacion de botones submit.
function boton(texto,href,clase,id){
    var btnAceptar = document.createElement("a");
    btnAceptar.setAttribute('type', 'submit');
    btnAceptar.setAttribute('id', id);
    btnAceptar.setAttribute('class', clase);
    btnAceptar.setAttribute('href', href);
    var textoBtn = document.createTextNode(texto);
    btnAceptar.appendChild(textoBtn);
    return btnAceptar
};