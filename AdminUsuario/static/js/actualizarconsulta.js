window.onload=function(){
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
                    console.log(json);
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
                        divInput.setAttribute('class', 'col-sm-10');
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
                        divInput.setAttribute('class', 'col-sm-10');
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

/*
let btnmas = document.getElementById('btnmas');

btnmas.addEventListener('click', () => {
    var form = document.getElementById('formupdate');
    
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
    inpDistribuidor.setAttribute('name', 'distribuidor[]');



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
    divInput.setAttribute('class', 'col-sm-10');
    //Input de Grupo Trabajo
    var inpGrupoTrabajo = document.createElement("input");
    inpGrupoTrabajo.setAttribute('class','form-control')
    inpGrupoTrabajo.setAttribute('id', 'campogrupo');
    inpGrupoTrabajo.setAttribute('name', 'grupotrabajo[]');

    //Button de Eliminacion Distribuidor - Grupo de Trabajo
    var btn = document.createElement("button");
    btn.setAttribute('type', 'button');
    btn.setAttribute('id', 'btneliminar');
    btn.setAttribute('class', 'btn btn-danger col-sm-2');
    btn.setAttribute('onclick', 'eliminar(this)')
    var btntexto = document.createTextNode("Eliminar");
    btn.append(btntexto);

    //Input para el identificador de relaciones
    var inputID = document.createElement("input");
    inputID.setAttribute('type', 'hidden');
    inputID.setAttribute('name', 'idDistribuidorGrupotrabajo[]');
    inputID.value = ""


    divInput.appendChild(inpGrupoTrabajo);
    divInputButton.appendChild(divInput);
    divInputButton.appendChild(btn);
    divcampGrupoTrabajo.appendChild(labelGrupoTrabajo);
    divcampGrupoTrabajo.appendChild(divInputButton);

    divcampdistribuidor.appendChild(labelDistribuidor);
    divcampdistribuidor.appendChild(inpDistribuidor);

    divDistribuidorGrupoTrabajo.appendChild(inputID);
    divDistribuidorGrupoTrabajo.appendChild(divcampdistribuidor);
    divDistribuidorGrupoTrabajo.appendChild(divcampGrupoTrabajo);

    form.insertBefore(divDistribuidorGrupoTrabajo,elementofinal);
})


const eliminar = (e) => {
    var form = document.getElementById('formupdate');
    elemtPadredivInputButton = e.parentNode;
    elemtPadredivGrupoTrabajo = elemtPadredivInputButton.parentNode;
    elemtPadredivDistribuidroGrupoTrabajo = elemtPadredivGrupoTrabajo.parentNode;
    form.removeChild(elemtPadredivDistribuidroGrupoTrabajo);
}
*/