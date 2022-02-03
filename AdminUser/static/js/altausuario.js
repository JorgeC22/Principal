window.onload=function(){
    
    var form = document.getElementById('forminsert');
    //var campo = document.getElementsByClassName('campodato');

    var inputgtrabajo = document.getElementById('msg_error');

   
    
    
    
    
    //var value = document.getElementById('searchInput').value;

}


/*for (var i=1; i=numInput;i++){
    var form = document.getElementById('forminsert');
    var inputgtrabajo = document.getElementById('msg_error');

    var pU = document.createElement("p");
    var texto = document.createTextNode('Grupo Trabajo #'+i);
    pU.appendChild(texto);
    var inp = document.createElement("input");
    form.insertBefore(inp,inputgtrabajo);
    form.insertBefore(pU,inp);
}*/
/*
numeroGT.oninput = function() {
    var form = document.getElementById('forminsert');
    
    numInput = numeroGT.value;
    console.log(numInput);

    for (var i=0;i==numInput;i++){
        if (i != 0){
            var indice = i - 1;
            var elementobefore = document.getElementById('parrafo'+String(indice));
        }else{
            var elementobefore = document.getElementById('msg_error');
        }

        var pU = document.createElement("p");
        pU.setAttribute('id', 'parrafo'+String(i));
        var texto = document.createTextNode("Grupo Trabajo #"+i);
        pU.appendChild(texto);
        var inp = document.createElement("input");
        inp.setAttribute('id', i);
        form.insertBefore(inp, elementobefore);
        form.insertBefore(pU, inp);
    }

    
};*/


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


