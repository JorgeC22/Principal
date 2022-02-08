window.onload = () => {
    var tit = document.getElementById('titulo');
    var elemento = document.getElementById('baset');

    let URLactual = document.URL;
    var URLnew = URLactual.replace("red", "blue/green");


    //tit.classList.add('newClass');
    tit.innerText = URLnew;
}