window.onload=function(){
    
    var form = document.getElementById('forminsert');
    //var campo = document.getElementsByClassName('campodato');

    var inputgtrabajo = document.getElementById('msg_error');

   
    
    
    
    
    //var value = document.getElementById('searchInput').value;

}



let btnmas = document.getElementById('btnmas');

btnmas.addEventListener('click', () => {
    var form = document.getElementById('forminsert');
    var elementofinal = document.getElementById('msg_error');
    var pU = document.createElement("p");
    pU.setAttribute('id', 'titlecamp');
    var texto = document.createTextNode("Grupo Trabajo");
    pU.appendChild(texto);
    var inp = document.createElement("input");
    inp.setAttribute('id', 'campogrupo');
    inp.setAttribute('name', 'grupotrabajo[]');
    form.insertBefore(inp,elementofinal);
    form.insertBefore(pU,inp);

})

let btnmenos = document.getElementById('btnmenos');

btnmenos.addEventListener('click', () => {
    var form = document.getElementById('forminsert');
    var campog = document.querySelectorAll('#campogrupo');
    var titlec = document.querySelectorAll('#titlecamp');
    console.log(campog.length);
    form.removeChild(campog[campog.length - 1]);
    form.removeChild(titlec[titlec.length - 1]);
    //form.removeChild(campog);

})


