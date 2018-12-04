$('#formularioUsuario').submit(function(e)
{
	console.log("CLICKY");
	e.preventDefault();
	$.ajax(
	{
		url: "http://localhost:8000/back/registrar",
		type: 'POST',
		dataType: "json",
		beforeSend: function (request) {
			request.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
		},
		data: $('#formularioUsuario').serialize(),
		success: function() {
			console.log('Usuario agregado con exito.');
			alert('Se ha registrado exitosamente')
		},
		error: function(errorThrown){
			console.log(errorThrown);
			alert('ERROR AL REGISTRAR USUARIO')
			}
	});
});

