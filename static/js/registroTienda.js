$('#FormTienda').submit(function(e)
{   
	console.log('Agregando Tienda...');
	e.preventDefault();
	$.ajax(
	{
		url:"http://localhost:8000/back/tienda",
		type:'POST',
		dataType: "json",
		beforeSend: function (request) {
			request.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
		},
		data: {'nombre_tienda': $("#id_nombre_tienda").val(),'nombre_sucursal':$("#id_nombre_sucursal").val(),'direccion':$("#id_direccion").val(),'region':$("#id_region").val(),'ciudad':$("#id_ciudad").val()},
        success: function (response) 
        {
            alert("Tienda agregada");
            console.log('Tienda agregada con exito');
		},
		error: function(errorThrown)
		{
			console.log(errorThrown);
		}
    })
    console.log($("#nombre_tienda"));
})
