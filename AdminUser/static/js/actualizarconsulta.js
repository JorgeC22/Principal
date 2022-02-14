window.onload=function(){
    usuarios();
    function usuarios(){
        let URLactual = document.URL;
        var URLnew = URLactual.replace("actualizarusuario", "consultaactualizar");
        

        var xhttp = new XMLHttpRequest();
        xhttp.open('GET',URLnew, true);
        xhttp.send();
        xhttp.onreadystatechange = function(){
            if(this.readyState==4 && this.status==200){
                var json = JSON.parse(this.responseText);
                var URLfuncion = URLactual.replace("actualizarusuario", "updateuser");
                
                var form = document.getElementById('formupdate');
                var elementofinal = document.getElementById('msg_error');
                var elemtnombreusuario = document.getElementById('nombreusuario');
                var elemtdistribuidor = document.getElementById('distribuidor');
                form.setAttribute('action', URLfuncion);
                
                for (var i=0;i<json.length;i++){
                    elemtnombreusuario.value = json[i].nombreusuario;
                    elemtdistribuidor.value = json[i].distribuidor;
                    
                    if (json[i].grupotrabajo === null){
                        console.log("No esta Registrado en ningun grupo de trabajo.")
                    }else{
                        islist = Array.isArray(json[i].grupotrabajo);
                        if (islist == true){
                            for (var j in json[i].grupotrabajo){
                                console.log(json[i].grupotrabajo[j].grupo)
                                if (json[i].grupotrabajo[j].grupo != null){
                                    var divInput = document.createElement("div");
                                    var pU = document.createElement("p");
                                    pU.setAttribute('id', 'titlecamp');
                                    var texto = document.createTextNode("Grupo Trabajo");
                                    pU.appendChild(texto);
                                    var inp = document.createElement("input");
                                    inp.setAttribute('id', 'campogrupo');
                                    inp.setAttribute('name', 'grupotrabajo[]');
                                    inp.value = json[i].grupotrabajo[j].grupo;
                                    //var inp2 = document.createElement("input");
                                    //inp2.setAttribute('id', 'extension');
                                    //inp2.setAttribute('name', 'extension[]');
                                    //inp2.setAttribute('type', 'hidden');
                                    //inp2.value = json[i].grupotrabajo[j].idrelacion;
                                    var btn = document.createElement("button");
                                    btn.setAttribute('type', 'button');
                                    btn.setAttribute('id', 'btneliminar');
                                    btn.setAttribute('onclick', 'eliminar(this)')
                                    var btntexto = document.createTextNode("Eliminar");
                                    btn.append(btntexto);
    
    
    
                                    divInput.appendChild(pU);
                                    divInput.appendChild(inp);
                                    //divInput.appendChild(inp2);
                                    divInput.appendChild(btn);
                                    form.insertBefore(divInput,elementofinal);
                                    
                                    
                                    //campo[cont].value = json[i].grupotrabajo[j];
                                }else{
                                    var pU = document.createElement("p");
                                    pU.setAttribute('id', 'titlecamp');
                                    var texto = document.createTextNode("Grupo Trabajo");
                                    pU.appendChild(texto);
                                    var inp = document.createElement("input");
                                    inp.setAttribute('id', 'campogrupo');
                                    inp.setAttribute('name', 'grupotrabajo[]');
                                    inp.setAttribute('placeholder', 'grupo');
                                    form.insertBefore(inp,elementofinal);
                                    form.insertBefore(pU,inp);
                                    //campo[cont].value = json[i].grupotrabajo[j];
                                }
                                
                            }
                        }else{
                            var divInput = document.createElement("div");
                            var pU = document.createElement("p");
                            pU.setAttribute('id', 'titlecamp');
                            var texto = document.createTextNode("Grupo Trabajo");
                            pU.appendChild(texto);
                            var inp = document.createElement("input");
                            inp.setAttribute('id', 'campogrupo');
                            inp.setAttribute('name', 'grupotrabajo[]');
                            var inp = document.createElement("input");
                            inp.setAttribute('id', 'campogrupo');
                            inp.setAttribute('name', 'grupotrabajo[]');
                            inp.value = json[i].grupotrabajo;
                            var btn = document.createElement("button");
                            btn.setAttribute('type', 'button');
                            btn.setAttribute('id', 'btneliminar');
                            btn.setAttribute('onclick', 'eliminar(this)')
                            var btntexto = document.createTextNode("Eliminar");
                            btn.append(btntexto);



                            divInput.appendChild(pU);
                            divInput.appendChild(inp);
                            divInput.appendChild(btn);
                            form.insertBefore(divInput,elementofinal);
                        }
                    }
                }
                
            }
        };
    }    
}


let btnmas = document.getElementById('btnmas');

btnmas.addEventListener('click', () => {
    var divInput = document.createElement("div");
    var form = document.getElementById('formupdate');
    var elementofinal = document.getElementById('msg_error');
    var pU = document.createElement("p");
    pU.setAttribute('id', 'titlecamp');
    var texto = document.createTextNode("Grupo Trabajo");
    pU.appendChild(texto);
    var inp = document.createElement("input");
    inp.setAttribute('id', 'campogrupo');
    inp.setAttribute('name', 'grupotrabajo[]');
    var btn = document.createElement("button");
    btn.setAttribute('type', 'button');
    btn.setAttribute('id', 'btneliminar');
    btn.setAttribute('onclick', 'eliminar(this)')
    var btntexto = document.createTextNode("Eliminar");
    btn.append(btntexto);
    
    
    divInput.appendChild(pU);
    divInput.appendChild(inp);
    divInput.appendChild(btn);
    form.insertBefore(divInput,elementofinal);

})


const eliminar = (e) => {
    var form = document.getElementById('formupdate');
    elemtPadre = e.parentNode;
    form.removeChild(elemtPadre);
    elemtPadre = '';
}
