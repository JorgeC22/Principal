window.onload=function(){
    usuarios();
    function usuarios(){
        var URLactual = document.URL;
        var URLnew = URLactual.replace("prueba", "numero");
        console.log(URLnew);

        var xhttp = new XMLHttpRequest();
        xhttp.open('GET',URLnew+"/2", true);
        xhttp.send();
        xhttp.onreadystatechange = function(){
            if(this.readyState==4 && this.status==200){
                var json = JSON.parse(this.responseText);
                console.log(json)
            }
        };
    }
}