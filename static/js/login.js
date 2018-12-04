$('#formLogin').submit(function(e)
{
	console.log("Autenticanddo...");
	e.preventDefault();
	$.ajax(
	{
		url:"http://localhost:8000/back/rest-auth/login/",
		type:'POST',
		dataType: "json",
		beforeSend: function (request) {
			request.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
		},
		data: $('#formLogin').serialize(),

		success: function (e) 
		{
			console.log("Se ha autenticado con exito");
			window.location = '/';
		},
		error: function(errorThrown){
			console.log(errorThrown);
			}
	})
})