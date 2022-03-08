function getAbsolutePath() {
    var loc = window.location;
    var pathName = loc.pathname.substring(0, loc.pathname.lastIndexOf('/') + 1);
    return loc.href.substring(0, loc.href.length - ((loc.pathname + loc.search + loc.hash).length - pathName.length));
}

let btnRegresar = document.getElementById('regresar');
btnRegresar.setAttribute("href",""+getAbsolutePath().slice(0, -1)+"");

var btnsearch = document.getElementById('btnsearch');

btnsearch.addEventListener('click', () => {
    
    var Nombre_search = document.getElementById('search').value;
    var URLactual = document.URL;
    var URLnew = URLactual.replace("modificarUsuario", "consultaUsuario");
        

    var form = document.getElementById('formModify');
    //var divbaseGeneralForms = document.getElementById('basegeneralForms') 
    var divBaseFormUsuario = document.getElementById('base_form');
    if (divBaseFormUsuario != null){
        form.removeChild(divBaseFormUsuario);
    }
    var msg = document.getElementById('msg_error');
    msg.textContent = "";

    var xhttp = new XMLHttpRequest();
    xhttp.open('GET',URLnew + '/' + Nombre_search, true);
    xhttp.send();
    xhttp.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){
            var json = JSON.parse(this.responseText);
            
            var URLfuncion = URLactual.replace("modificarUsuario", "actualizarUsuario");
            var URLfuncionEliminar = URLactual.replace("modificarUsuario", "eliminarUsuario");
            form.setAttribute('action', URLfuncion);

            
            for (var i=0;i<json.length;i++){

                if (json[i].status != "true"){
                    var textoMsg = document.createTextNode("Error: El nombre usuario especificado no existe.");
                    msg.appendChild(textoMsg);
                }else{
                    //Base de Formulario
                var divBaseForm = document.createElement("div");
                divBaseForm.setAttribute('id', 'base_form');
                
                //Seccion del Nombre de usuario
                var divNombre = document.createElement("div");
                divNombre.setAttribute('class', 'mb-3');
                var labelNombre = document.createElement("label");
                var textoNombre = document.createTextNode("Nombre Usuario");
                labelNombre.appendChild(textoNombre);
                labelNombre.setAttribute('class', 'col-form-label');
                var inputNombre = document.createElement("input");
                inputNombre.setAttribute('class', 'form-control');
                inputNombre.setAttribute('name', 'nombre_usuario');
                inputNombre.setAttribute('type', 'text');
                inputNombre.value = json[i].nombreusuario

                //Seccion del Ruta
                var divRuta = document.createElement("div");
                divRuta.setAttribute('class', 'mb-3');
                var labelRuta = document.createElement("label");
                var textoRuta = document.createTextNode("Ruta de Acceso");
                labelRuta.appendChild(textoRuta);
                labelRuta.setAttribute('class', 'col-form-label');
                var inputRuta = document.createElement("input");
                inputRuta.setAttribute('class', 'form-control');
                inputRuta.setAttribute('name', 'ruta');
                inputRuta.setAttribute('type', 'text');
                inputRuta.value = json[i].ruta

                //Button Agregar Distribuidor - Grupo de Trabajo
                var btnMAS = document.createElement("button");
                btnMAS.setAttribute('type', 'button');
                btnMAS.setAttribute('id', 'btnmas');
                btnMAS.setAttribute('class', 'btn btn-success mb-3');
                btnMAS.setAttribute('onclick', 'crearDominio()')
                var btntexto = document.createTextNode("Agregar Distribuidor - Grupo de trabajo");
                btnMAS.append(btntexto);

                //Input para el identificador del usuario
                var inputIDusuario = document.createElement("input");
                inputIDusuario.setAttribute('type', 'hidden');
                inputIDusuario.setAttribute('name', 'idusuario');
                inputIDusuario.value = json[i].id_usuario

                //Formulario para la eliminacion de Usuario
                var formBtnEliminar = document.createElement("form");
                formBtnEliminar.setAttribute('id', 'formEliminarUsuario');
                formBtnEliminar.setAttribute('action', URLfuncionEliminar);
                formBtnEliminar.setAttribute('method', 'POST');
                
                //Button Eliminar Usuario
                var btnMIN = document.createElement("button");
                btnMIN.setAttribute('type', 'Submit');
                btnMIN.setAttribute('id', 'btnmin');
                btnMIN.setAttribute('name', 'identificador')
                btnMIN.setAttribute('class', 'btn btn-danger mb-3');
                var btntexto = document.createTextNode("Eliminar Usuario");
                btnMIN.append(btntexto);
                btnMIN.value = json[i].id_usuario

                formBtnEliminar.appendChild(btnMIN);
                divNombre.appendChild(inputIDusuario);
                divNombre.appendChild(labelNombre);
                divNombre.appendChild(inputNombre);

                divRuta.appendChild(labelRuta);
                divRuta.appendChild(inputRuta);

                divBaseForm.appendChild(divNombre);
                divBaseForm.appendChild(divRuta);
                divBaseForm.appendChild(btnMAS)
                
                divBaseForm.appendChild(formBtnEliminar);

                
                
                islist = Array.isArray(json[i].distribuidorgrupotrabajo);
                if (islist == true){
                    for (var j=0;j<json[i].distribuidorgrupotrabajo.length;j++){
                        if (json[i].distribuidorgrupotrabajo[j].grupotrabajo == null){
                            
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
                            inpDistribuidor.value = json[i].distribuidorgrupotrabajo[j].distribuidor



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
                            inputID.value = json[i].distribuidorgrupotrabajo[j].id_distribuidor_grupotrabajo

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

                            divBaseForm.appendChild(divDistribuidorGrupoTrabajo)
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
                            inpDistribuidor.setAttribute('name', 'distribuidor[]');
                            inpDistribuidor.value = json[i].distribuidorgrupotrabajo[j].distribuidor



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
                            inpGrupoTrabajo.value = json[i].distribuidorgrupotrabajo[j].grupotrabajo

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
                            inputID.value = json[i].distribuidorgrupotrabajo[j].id_distribuidor_grupotrabajo

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

                            divBaseForm.appendChild(divDistribuidorGrupoTrabajo)
                        }
                    }
                }else{
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
                        inpDistribuidor.setAttribute('name', 'distribuidor[]');
                        inpDistribuidor.value = json[i].distribuidorgrupotrabajo.distribuidor;



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
                        inputID.value = json[i].distribuidorgrupotrabajo.id_distribuidor_grupotrabajo

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

                        divBaseForm.appendChild(divDistribuidorGrupoTrabajo)
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
                        inpDistribuidor.setAttribute('name', 'distribuidor[]');
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
                        inpGrupoTrabajo.setAttribute('name', 'grupotrabajo[]');
                        inpGrupoTrabajo.value = json[i].distribuidorgrupotrabajo.grupotrabajo

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
                        inputID.value = json[i].distribuidorgrupotrabajo.id_distribuidor_grupotrabajo

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

                        divBaseForm.appendChild(divDistribuidorGrupoTrabajo)
                    }
                }
                
                form.insertBefore(divBaseForm,elementofinal);
              
                }

                
                 
            } 
            
        }
    };   
})



const crearDominio = (e) => {
    var form = document.getElementById('formModify');
    var divBaseFormReal = document.getElementById('base_form');

    
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

    divBaseFormReal.appendChild(divDistribuidorGrupoTrabajo);
}

const eliminar = (e) => {
    var divBaseForm = document.getElementById('base_form');
    elemtPadredivInputButton = e.parentNode;
    elemtPadredivGrupoTrabajo = elemtPadredivInputButton.parentNode;
    elemtPadredivDistribuidroGrupoTrabajo = elemtPadredivGrupoTrabajo.parentNode;
    divBaseForm.removeChild(elemtPadredivDistribuidroGrupoTrabajo);
}