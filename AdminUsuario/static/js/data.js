//JavaScript File
window.onload=function(){
    //Menú de opciones de acuerdo al tipo movimiento - periodo
    document.getElementById("abono21").addEventListener("click",function(){ tipoMovimiento(this); });
    document.getElementById("abono22").addEventListener("click",function(){ tipoMovimiento(this); });
    document.getElementById("comision21").addEventListener("click",function(){ tipoMovimiento(this); });
    document.getElementById("comision22").addEventListener("click",function(){ tipoMovimiento(this); });
    //Limpiar tabla cuando se eliga otra opcion y se carguen los nuevos datos
    function eliminarElementos(){
        var elemento = document.getElementById("mensaje");
		while(elemento.firstChild){
            elemento.removeChild(elemento.firstChild);
		}
        var elemento = document.getElementById("data");
		while(elemento.firstChild){
            elemento.removeChild(elemento.firstChild);
		}
    }
    //De acuerdo al tipo de movimiento seleccionado se completa la ruta y se llama a la funcion movimientos
    function tipoMovimiento(objeto){
        var ruta = window.location.pathname;
		switch(objeto.id){
			case 'abono21':
                eliminarElementos();
				ruta = "http://127.0.0.1:5000" + ruta +'/30/2021';
                movimientos(ruta);
				break;
            case 'abono22':
                eliminarElementos();
                ruta = "http://127.0.0.1:5000" + ruta +'/30/2022';
                movimientos(ruta);
                break;
			case 'comision21':
                eliminarElementos();
				ruta = "http://127.0.0.1:5000" + ruta +'/34/2021';
                movimientos(ruta);
				break;
            case 'comision22':
                eliminarElementos();
                ruta = "http://127.0.0.1:5000" + ruta +'/34/2022';
                movimientos(ruta);
                break;
			default:
		}
	}
    //Funcion que hace una peticion get al servidor y estrucutura la data en foma de tabla
    function movimientos(ruta){
        //Declaracion del metodo XMLHttpRequest
        const xhttp = new XMLHttpRequest();
        //Indicamos el tipo de la peticion, URL, true si sera constante
        xhttp.open('GET',ruta,true);
        //Se envia la peticion
        xhttp.send();
        //Obtenemos el estado y status de la respuesta del servidor
        xhttp.onreadystatechange = function(){
            //Si el estado es 4 y estatus es igual a 200
            if(this.readyState==4 && this.status==200){
                //Almacenamos la respuesta en json convertiendola en formato JSON
                const json = JSON.parse(this.responseText);
                //Obtenemos el nodo movimientos de json
                const {movimientos} = json;
                //Si devuelve una respuesta vacia se muestra el siguiente mensaje
                if(movimientos.length == 0){
                    var texto = document.createTextNode("No existen movimientos en el periodo seleccionado");
                    document.getElementById("mensaje").appendChild(texto);
                }
                //De lo contrario agrega elementos al DOM HTML, creacion de la tabla
                else{
                    var tabla = document.createElement("table");
                    tabla.setAttribute("class","table table-striped table-sm");
                    tabla.setAttribute("style","font-size:11px");
                    tabla.setAttribute("id","tabla");
                    document.getElementById("data").appendChild(tabla)
                    var encabezado = document.createElement("thead");
                    encabezado.setAttribute("id","titulos");
                    document.getElementById("tabla").appendChild(encabezado);
                    var fila = document.createElement("tr");
                    fila.setAttribute("id","encabezado");
                    document.getElementById("titulos").appendChild(fila);
                    var cuerpo = document.createElement("tbody");
                    cuerpo.setAttribute("id","res");
                    document.getElementById("tabla").appendChild(cuerpo);
                    //Lista con los titulos de la tabla
                    var titulos =  ['Distribuidor','Grupo Trabajo','Empresa','ID Cuenta Ahorro','Enero','Febrero','Marzo','Abril','Mayo','Junio',
                    'Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre','Total Generado']
                    //Genera elementos HTML al DOM, crea cada columna de la tabla con su respectivo titulo
                    for(var i of titulos){
                        var columna = document.createElement("th");
                        var texto = document.createTextNode(i);
                        columna.appendChild(texto);
                        document.getElementById("encabezado").appendChild(columna);
                    
                    } 
                    //Declaracion de una variable para hacer la suma de cada uno de los montos hechos por cada mes
                    var total = 0;
                    //Recorremos cada una de las posiciones de movimientos
                    for (var i=0;i<movimientos.length;i++){
                        //Genera elementos HTML al DOM, pasandole el valor de cada una de las etiquetas el contenido de movimientos indicando 
                        //que elemento tomara de la lista de json contenidas en el
                        var renglon = document.createElement("tr");
                        renglon.setAttribute("id",movimientos[i].id_cuenta_ahorro)
                        document.getElementById("res").appendChild(renglon);
                        var celda = document.createElement("td");
                        var texto = document.createTextNode(movimientos[i].distribuidor);
                        celda.appendChild(texto);
                        document.getElementById(movimientos[i].id_cuenta_ahorro).appendChild(celda);
                        var celda = document.createElement("td");
                        var texto = document.createTextNode(movimientos[i].grupo_trabajo);
                        celda.appendChild(texto);
                        document.getElementById(movimientos[i].id_cuenta_ahorro).appendChild(celda);
                        var celda = document.createElement("td");
                        var texto = document.createTextNode(movimientos[i].empresa);
                        celda.appendChild(texto);
                        document.getElementById(movimientos[i].id_cuenta_ahorro).appendChild(celda);
                        var celda = document.createElement("td");
                        var texto = document.createTextNode(movimientos[i].id_cuenta_ahorro);
                        celda.appendChild(texto);
                        document.getElementById(movimientos[i].id_cuenta_ahorro).appendChild(celda);
                        //Genera elementos HTML al DOM, crea para cada columna que corresponde a un mes se le asigna un id que lleva el id_cuenta_ahorro
                        //del producto seguido de un guion bajo y el numero de mes
                        for(var j=1;j<=12;j++){
                            var celda = document.createElement("td");
                            celda.setAttribute("id", movimientos[i].id_cuenta_ahorro+'_'+j);
                            document.getElementById(movimientos[i].id_cuenta_ahorro).appendChild(celda);
                        }
                        //Recorremos cada una de las posiciones contenidas en el elemento movimiento dentro de movimientos
                        for (var j=0;j<movimientos[i].movimiento.length;j++){
                            //Genera elementos HTML al DOM, si el id del elemento coincide con el ultimo caracter coloca el resultado en la celda 
                            //que le corresponde
                            var celda = document.getElementById(movimientos[i].id_cuenta_ahorro + '_' + movimientos[i].movimiento[j].mes);
                            var texto = document.createTextNode(new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(parseFloat(movimientos[i].movimiento[j].monto).toFixed(2)));
                            celda.appendChild(texto);
                            //Suma recurrente entre cada monto de cada celda, se convierte a double el string de monto
                            total = total + parseFloat(movimientos[i].movimiento[j].monto);
                        }
                        //Genera elementos HTML al DOM, columna correspondiente a la suma total de cada monto por cada producto
                        var celda = document.createElement("td");
                        var texto = document.createTextNode(new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(parseFloat(total).toFixed(2)));
                        celda.appendChild(texto);
                        document.getElementById(movimientos[i].id_cuenta_ahorro).appendChild(celda);
                        //Iniciamos el valor de total en cero
                        total = 0;
                    }
                    //Creacion de los elementos de pie de pagina de la tabla para mostrar el total de cada columna correspondiente a los meses
                    var elemento = document.createElement("tfoot");
                    elemento.setAttribute("id","total");
                    document.getElementById("tabla").appendChild(elemento);
                    var elemento = document.createElement("tr");
                    elemento.setAttribute("id","suma");
                    document.getElementById("total").appendChild(elemento);
                    for(var i=0;i<=16;i++){
                        var columna = document.createElement("th");
                        document.getElementById("suma").appendChild(columna);
                    }
                    //Se llama a la libreria de Datatables para darle formato a la tabla y mostrar las opciones: boton, filtro, informacion, paginacion
                    $(function() {
                        $('#tabla').DataTable( {
                            language: {
                                url: "https://cdn.datatables.net/plug-ins/1.10.15/i18n/Spanish.json"
                            },
                            dom: "<'row'<'col-sm-12 col-md-11'f><'col-sm-12 col-md-1'B>>" +
                                 "<'row'<'col-sm-12'tr>>" +
                                 "<'row'<'col-sm-12 col-md-6'li><'col-sm-12 col-md-6'p>>",
                            buttons: [
                                {
                                    extend: 'excel',
                                    footer: true,
                                    excelStyles: {
                                        //Seleccion del rango de columnas para definir el tipo de dato a moneda cuando se haga la exportacion de la tabla
                                        cells: 'E:Q',
                                        style: {
                                            numFmt: "[$$-en-ES] #,##0.00"
                                        }
                                    },
                                    text:      '<i class="fas fa-file-excel"></i> ',
                                    titleAttr: 'Exportar a Excel',
                                    className: 'btn btn-success'
                                }
                            ],
                            footerCallback: function ( row, data, start, end, display ) {
                                var api = this.api();
                                //Elimina los caracteres especiales para obtener un valor númerico 
                                var valor = function ( i ) {
                                    return typeof i === 'string' ?
                                        i.replace(/[\$,]/g, '')*1 :
                                        typeof i === 'number' ?
                                            i : 0;
                                };
                                $( api.column( 3 ).footer() ).html('Total');
                                // Realiza la suma total de cada columna-renglon y la muestra en la posicion del pie de pagina de la tabla
                                for(var i=4;i<=16;i++){
                                    var total = api
                                        .column(i)
                                        .data()
                                        .reduce( function (a, b) {
                                            return valor(a) + valor(b);
                                        }, 0);
                                    if (total != 0){
                                        total = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(parseFloat(total).toFixed(2));
                                    }
                                    else{
                                        total = "";
                                    }
                                    $( api.column( i ).footer() ).html(total);
                                } 
                            }
                        } );
                    } );
                }
            }
        }
    }
}