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
                console.log(json);
                var URLfuncion = URLactual.replace("actualizarusuario", "updateuser");
                
                var form = document.getElementById('formupdate');
                var elementofinal = document.getElementById('msg_error');
                var primergrupo = document.getElementById('campogrupoprincipal');
                var campo = document.querySelectorAll('.campodato')
                form.setAttribute('action', URLfuncion)
                
                for (var i=0;i<json.length;i++){
                    campo[0].value = json[i].nombreusuario;
                    campo[1].value = json[i].distribuidor;
                    cont = 2;
                    if (json[i].grupotrabajo.length > 1){
                        for (var j in json[i].grupotrabajo){
                            var pU = document.createElement("p");
                            pU.setAttribute('id', 'titlecamp');
                            var texto = document.createTextNode("Grupo Trabajo");
                            pU.appendChild(texto);
                            var inp = document.createElement("input");
                            inp.setAttribute('id', 'campogrupo');
                            inp.setAttribute('name', 'grupotrabajo[]');
                            inp.value = json[i].grupotrabajo[j];
                            form.insertBefore(inp,campo[1]);
                            form.insertBefore(pU,inp);
                            //campo[cont].value = json[i].grupotrabajo[j];
                            cont++;
                        }
                    }
                }
                
            }
        };
    }
}




