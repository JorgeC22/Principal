window.onload=function(){
    usuarios();
    function usuarios(){
        var URLactual = document.URL;
        var URLnew = URLactual.replace("validar", "consultaDatos");
        console.log(URLnew);

        var xhttp = new XMLHttpRequest();
        xhttp.open('GET',URLnew, true);
        xhttp.send();
        xhttp.onreadystatechange = function(){
            if(this.readyState==4 && this.status==200){
                var json = JSON.parse(this.responseText);

                var tbody = document.getElementById('base_datos');
                
                for (let i = 0; i < json.documentos.length; i++) {
                    
                    console.log(json.documentos[i].campo)

                    var fila = document.createElement("tr");
                    var campo = document.createElement("td");
                    var textofila = document.createTextNode(json.documentos[i].campo);
                    campo.appendChild(textofila);

                    var ruta = document.createElement("td");
                    var textofila = document.createTextNode(json.documentos[i].rutaS3);
                    ruta.appendChild(textofila);

                    var btnAceptar = document.createElement("td");
                    var inputAceptar = document.createElement("input");
                    inputAceptar.setAttribute('type', 'radio');
                    inputAceptar.setAttribute('name', json.documentos[i].campo);
                    inputAceptar.setAttribute('value', 'aprobado');
                    btnAceptar.appendChild(inputAceptar);

                    var btnRechazar = document.createElement("td");
                    var inputRechazar = document.createElement("input");
                    inputRechazar.setAttribute('type', 'radio');
                    inputRechazar.setAttribute('name', json.documentos[i].campo);
                    inputRechazar.setAttribute('value', 'rechazado');
                    btnRechazar.appendChild(inputRechazar);
                    


                    fila.append(campo);
                    fila.append(ruta);
                    fila.append(btnAceptar);
                    fila.append(btnRechazar);

                    tbody.append(fila);
                }
                    
            }
        }
    }
}