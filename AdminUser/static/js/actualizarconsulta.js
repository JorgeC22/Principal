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
                    
                    if (json[i].grupotrabajo.length > 1){
                        for (var j in json[i].grupotrabajo){
                            console.log(json[i].grupotrabajo[j].grupo)
                            if (json[i].grupotrabajo[j].grupo != null){
                                var pU = document.createElement("p");
                                pU.setAttribute('id', 'titlecamp');
                                var texto = document.createTextNode("Grupo Trabajo");
                                pU.appendChild(texto);
                                var inp = document.createElement("input");
                                inp.setAttribute('id', 'campogrupo');
                                inp.setAttribute('name', 'grupotrabajo[]');
                                inp.value = json[i].grupotrabajo[j].grupo;
                                form.insertBefore(inp,elementofinal);
                                form.insertBefore(pU,inp);
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
                        var pU = document.createElement("p");
                            pU.setAttribute('id', 'titlecamp');
                            var texto = document.createTextNode("Grupo Trabajo");
                            pU.appendChild(texto);
                            var inp = document.createElement("input");
                            inp.setAttribute('id', 'campogrupo');
                            inp.setAttribute('name', 'grupotrabajo[]');
                            inp.value = json[i].grupotrabajo.grupo;
                            form.insertBefore(inp,elementofinal);
                            form.insertBefore(pU,inp);
                    }
                }
                
            }
        };
    }
}




