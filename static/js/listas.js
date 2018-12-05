$(document).ready(function()
{
	console.log("CREANDO TABLE");	
	$.ajax(
	{

		url: "http://localhost:8000/back/lista",
		type: 'GET',

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
							<th></th>\
						</tr>\
					</thead>"
			);

			
			$.each(result,function(i,items)
			{
				$("#tablePreview").append('<tr>');
				$("#tablePreview").append("<th scope='row'> <a href=\"/listaProductos/"+result[i].codigo_lista+"/\">"+result[i].nombre_lista+"</a></th>");
				$("#tablePreview").append("<th scope='row'>"+i+"</th>");
				$("#tablePreview").append("<th scope='row'>"+i+"</th>");
				$("#tablePreview").append("<th scope='row'>"+i+"</th>");
				$("#tablePreview").append("<th scope='row'>");
				$("#tablePreview").append("<a class='btn btn-secondary' href=\"/agregarProductos/"+result[i].codigo_lista+"/\" role='button'>Comprar</a>");
				$("#tablePreview").append("</th>");
				$("#tablePreview").append("</tr>");
				$("#tablePreview").append("</tbody>");         
			});
		}
	}); 
})
