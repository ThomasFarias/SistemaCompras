$("#formTienda").submit(function(){   
    $.ajax({
    url:"http://localhost:8000/back/tienda/",
    type:'POST',
    data: {'nombre_tienda': $("#nombre_tienda").val(),'nombre_sucursal':$("#nombre_sucursal").val(),'direccion':$("#direccion").val(),'region':$("#region").val(),'ciudad':$("#ciudad").val(),'estado':false},
    success: function (response) {
    alert("exito al ingresar");
            }
        })
        })
       