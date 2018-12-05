$(document).ready(function()
{
	console.log("CREANDO TABLE");	
	$.ajax(
	{
		url: "http://localhost:8000/back/lista",
		success: function(result)
		{
			console.log("CREANDO TABLE 2");	
			$('#tablacompras').append("Listas de compras");
			$('#tablacompras').append(
				"<table id='tablePreview' class='table table-striped table-bordered'>\
					<thead>\
						<tr>\
							<th>Lista</th>\
							<th>Total Productos</th>\
							<th>Productos Comprados</th>\
							<th>Presupuestado</th>\
							<th>Costo Real</th>\
						</tr>\
					</thead>"
			);
			$.each(result,function(i,items)
			{
				$("#tablePreview").append('<tr>');
				$("#tablePreview").append("<th scope='row'>"+result[i].nombre_lista+"</th>")
				$("#tablePreview").append("<th scope='row'>"+i+"</th>")
				$("#tablePreview").append("<th scope='row'>"+i+"</th>")
				$("#tablePreview").append("<th scope='row'>"+i+"</th>")
				$("#tablePreview").append("<th scope='row'>"+i+"</th>")


				$("#tablePreview").append("</tr>");
				$("#tablePreview").append("</tbody>");         
			});
		}
	}); 
})
