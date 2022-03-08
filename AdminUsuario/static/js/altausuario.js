function getAbsolutePath() {
    var loc = window.location;
    var pathName = loc.pathname.substring(0, loc.pathname.lastIndexOf('/') + 1);
    return loc.href.substring(0, loc.href.length - ((loc.pathname + loc.search + loc.hash).length - pathName.length));
}

let btnRegresar = document.getElementById('regresar');
btnRegresar.setAttribute("href",""+getAbsolutePath().slice(0, -1)+"");

let btnReturn = document.getElementById('return');
btnReturn.setAttribute("href",""+getAbsolutePath().slice(0, -1)+"");

let actForm = document.getElementById('forminsert');
actForm.setAttribute('action',''+getAbsolutePath().slice(0, -1)+'/insertarusuario');

let btnmas = document.getElementById('btnmas');

btnmas.addEventListener('click', () => {
    var form = document.getElementById('forminsert');
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

    divInput.appendChild(inpGrupoTrabajo);
    divInputButton.appendChild(divInput);
    divInputButton.appendChild(btn);
    divcampGrupoTrabajo.appendChild(labelGrupoTrabajo);
    divcampGrupoTrabajo.appendChild(divInputButton);

    divcampdistribuidor.appendChild(labelDistribuidor);
    divcampdistribuidor.appendChild(inpDistribuidor);

    divDistribuidorGrupoTrabajo.appendChild(divcampdistribuidor);
    divDistribuidorGrupoTrabajo.appendChild(divcampGrupoTrabajo);

    form.insertBefore(divDistribuidorGrupoTrabajo,elementofinal);

})


const eliminar = (e) => {
    var form = document.getElementById('forminsert');
    elemtPadredivInputButton = e.parentNode;
    elemtPadredivGrupoTrabajo = elemtPadredivInputButton.parentNode;
    elemtPadredivDistribuidroGrupoTrabajo = elemtPadredivGrupoTrabajo.parentNode;
    form.removeChild(elemtPadredivDistribuidroGrupoTrabajo);
}
