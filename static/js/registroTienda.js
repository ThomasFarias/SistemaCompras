$("#formTienda").submit(function(){   
    $.ajax({
    url:"http://localhost:8000/back/tienda/",
    type:'POST',
    data: {'nombre_tienda': $("#id_nombre_tienda").val(),'nombre_sucursal':$("#id_nombre_sucursal").val(),'direccion':$("#id_direccion").val(),'region':$("#id_region").val(),'ciudad':$("#id_ciudad").val()},
    success: function (response) {
    alert("exito al ingresar");
            }
        })
        })
       