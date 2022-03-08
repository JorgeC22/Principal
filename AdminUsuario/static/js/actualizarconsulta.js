window.onload=function(){
    function dividirCadena(ruta,separador) {
        var array = ruta.split(separador);
        return array[1];
    }
    var ruta = window.location.pathname;
    var btnRegresar = document.getElementById('regresar');
    btnRegresar.setAttribute("href","http://127.0.0.1:5000/"+dividirCadena(ruta, '/')+"");

    usuarios();
    function usuarios(){
        let URLactual = document.URL;
        var URLnew = URLactual.replace("actualizarRegistro", "consultaactualizar");
        

        var xhttp = new XMLHttpRequest();
        xhttp.open('GET',URLnew, true);
        xhttp.send();
        xhttp.onreadystatechange = function(){
            if(this.readyState==4 && this.status==200){
                var json = JSON.parse(this.responseText);
                var URLfuncion = URLactual.replace("actualizarRegistro", "actualizarDistribuidorGrupotrabajo");
                
                var form = document.getElementById('formupdate');
                var elementofinal = document.getElementById('msg_error');
                var elemtnombreusuario = document.getElementById('nombre_usuario');
                form.setAttribute('action', URLfuncion);
                
                for (var i=0;i<json.length;i++){
                    elemtnombreusuario.value = json[i].nombreusuario;
                    elemtnombreusuario.setAttribute('readonly','');
                    //campo[cont].value = json[i].grupotrabajo[j];
                    //inp.value = json[i].grupotrabajo[j].grupo;
                    //islist = Array.isArray(json[i].distribuidorgrupotrabajo);
                    //for (var j in json[i].distribuidorgrupotrabajo){
                    
                    
                    if (json[i].distribuidorgrupotrabajo.grupotrabajo == null){
                            
                        //Div base del registro Distribuidor - Grupo de Trabajo
                        var divDistribuidorGrupoTrabajo = document.createElement("div");
                        divDistribuidorGrupoTrabajo.setAttribute('class', 'row');
                        //Elemento de referencia.
                        var elementofinal = document.getElementById('msg_error');
                        
                        //Div de distribuidor
                        var divcampdistribuidor = document.createElement("div");
                        divcampdistribuidor.setAttribute('class', 'mb-3 col-sm-6');
                        //Label de distribuidor
                        var labelDistribuidor = document.createElement("label");
                        labelDistribuidor.setAttribute('class', 'col-form-label');
                        var textoDistribuidor = document.createTextNode("Distribuidor");
                        labelDistribuidor.appendChild(textoDistribuidor);
                        //Input de Distribuidor
                        var inpDistribuidor = document.createElement("input");
                        inpDistribuidor.setAttribute('class','form-control')
                        inpDistribuidor.setAttribute('id', 'campogrupo');
                        inpDistribuidor.setAttribute('name', 'distribuidor');
                        inpDistribuidor.value = json[i].distribuidorgrupotrabajo.distribuidor



                        //Div de Grupo Trabajo
                        var divcampGrupoTrabajo = document.createElement("div");
                        divcampGrupoTrabajo.setAttribute('class', 'mb-3 col-sm-6');
                        //Label de Grupo Trabajo
                        var labelGrupoTrabajo = document.createElement("label");
                        labelGrupoTrabajo.setAttribute('class', 'col-form-label');
                        var textoGrupoTrabajo = document.createTextNode("Grupo de Trabajo");
                        labelGrupoTrabajo.appendChild(textoGrupoTrabajo);
                        //Div Input & Button
                        var divInputButton = document.createElement("div");
                        divInputButton.setAttribute('class', 'row');
                        //Div de Input Grupo Trabajo
                        var divInput = document.createElement("div");
                        divInput.setAttribute('class', 'col-sm-12');
                        //Input de Grupo Trabajo
                        var inpGrupoTrabajo = document.createElement("input");
                        inpGrupoTrabajo.setAttribute('class','form-control')
                        inpGrupoTrabajo.setAttribute('id', 'campogrupo');
                        inpGrupoTrabajo.setAttribute('name', 'grupotrabajo');

                        

                        divInput.appendChild(inpGrupoTrabajo);
                        divInputButton.appendChild(divInput);
                        divcampGrupoTrabajo.appendChild(labelGrupoTrabajo);
                        divcampGrupoTrabajo.appendChild(divInputButton);

                        divcampdistribuidor.appendChild(labelDistribuidor);
                        divcampdistribuidor.appendChild(inpDistribuidor);

                        divDistribuidorGrupoTrabajo.appendChild(divcampdistribuidor);
                        divDistribuidorGrupoTrabajo.appendChild(divcampGrupoTrabajo);

                        form.insertBefore(divDistribuidorGrupoTrabajo,elementofinal);
                    }
                    else{
                        //Div base del registro Distribuidor - Grupo de Trabajo
                        var divDistribuidorGrupoTrabajo = document.createElement("div");
                        divDistribuidorGrupoTrabajo.setAttribute('class', 'row');
                        //Elemento de referencia.
                        var elementofinal = document.getElementById('msg_error');
                        
                        //Div de distribuidor
                        var divcampdistribuidor = document.createElement("div");
                        divcampdistribuidor.setAttribute('class', 'mb-3 col-sm-6');
                        //Label de distribuidor
                        var labelDistribuidor = document.createElement("label");
                        labelDistribuidor.setAttribute('class', 'col-form-label');
                        var textoDistribuidor = document.createTextNode("Distribuidor");
                        labelDistribuidor.appendChild(textoDistribuidor);
                        //Input de Distribuidor
                        var inpDistribuidor = document.createElement("input");
                        inpDistribuidor.setAttribute('class','form-control')
                        inpDistribuidor.setAttribute('id', 'campogrupo');
                        inpDistribuidor.setAttribute('name', 'distribuidor');
                        inpDistribuidor.value = json[i].distribuidorgrupotrabajo.distribuidor



                        //Div de Grupo Trabajo
                        var divcampGrupoTrabajo = document.createElement("div");
                        divcampGrupoTrabajo.setAttribute('class', 'mb-3 col-sm-6');
                        //Label de Grupo Trabajo
                        var labelGrupoTrabajo = document.createElement("label");
                        labelGrupoTrabajo.setAttribute('class', 'col-form-label');
                        var textoGrupoTrabajo = document.createTextNode("Grupo de Trabajo");
                        labelGrupoTrabajo.appendChild(textoGrupoTrabajo);
                        //Div Input & Button
                        var divInputButton = document.createElement("div");
                        divInputButton.setAttribute('class', 'row');
                        //Div de Input Grupo Trabajo
                        var divInput = document.createElement("div");
                        divInput.setAttribute('class', 'col-sm-12');
                        //Input de Grupo Trabajo
                        var inpGrupoTrabajo = document.createElement("input");
                        inpGrupoTrabajo.setAttribute('class','form-control')
                        inpGrupoTrabajo.setAttribute('id', 'campogrupo');
                        inpGrupoTrabajo.setAttribute('name', 'grupotrabajo');
                        inpGrupoTrabajo.value = json[i].distribuidorgrupotrabajo.grupotrabajo

                        

                     

                        divInput.appendChild(inpGrupoTrabajo);
                        divInputButton.appendChild(divInput);
                        divcampGrupoTrabajo.appendChild(labelGrupoTrabajo);
                        divcampGrupoTrabajo.appendChild(divInputButton);

                        divcampdistribuidor.appendChild(labelDistribuidor);
                        divcampdistribuidor.appendChild(inpDistribuidor);

                        divDistribuidorGrupoTrabajo.appendChild(divcampdistribuidor);
                        divDistribuidorGrupoTrabajo.appendChild(divcampGrupoTrabajo);

                        form.insertBefore(divDistribuidorGrupoTrabajo,elementofinal);
                    }
                }    
                
                
            }
        };
    }    
}