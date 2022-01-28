window.onload=function(){
    usuarios();
    function usuarios(){
        var xhttp = new XMLHttpRequest();
        xhttp.open('GET','http://127.0.0.1:5000/consultaactualizar', true);
        xhttp.send();
        xhttp.onreadystatechange = function(){
            if(this.readyState==4 && this.status==200){
                var res = JSON.parse(this.responseText);

                
                var campo = document.querySelectorAll('.campo');

                for (var items of campo){
                    var texto = document.createTextNode(res[0]);
                    items[0].appendChild(texto);
                }
                
            }
        };
    }
}



