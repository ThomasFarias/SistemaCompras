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
		data: {'nombre_tienda': $("#nombre_tienda").val(),'nombre_sucursal':$("#nombre_sucursal").val(),'direccion':$("#direccion").val(),'region':$("#region").val(),'ciudad':$("#ciudad").val()},
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
       