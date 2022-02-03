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
                
                var campo = document.getElementsByClassName('campodato');
                var celda = document.getElementById('formulario_update');
                celda.setAttribute('action', URLfuncion)
                
                for (var i=0;i<json.length;i++){
                    campo[0].value = json[i].username;
                    campo[1].value = json[i].distribuidor;
                    campo[2].value = json[i].grupotrabajo;

                }
                
            }
        };
    }
}



