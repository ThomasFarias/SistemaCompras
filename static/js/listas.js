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
			
			$.each(result,function(i,lista)
			{
				var total_productos = 0;
				var productos_comprados = 0;
				var presupuestado =0;
				var costo_real =0;
				$.ajax(
				{
					url: "http://localhost:8000/back/producto",
					type: 'GET',
					success: function(resultado)
					{
						$.each(resultado,function(x,producto)
						{

							if(producto.lista == lista.codigo_lista)
							{

								total_productos = total_productos+1;
								presupuestado = presupuestado + producto.costo_presupuestado;
								if(producto.costo_real > 0)
								{
									productos_comprados = productos_comprados+1;
								}
								costo_real = costo_real + producto.costo_real;
								
							}
						});
						console.log(total_productos);
						$("#tablePreview").append('<tr>');
						$("#tablePreview").append("<th scope='row'> <a href=\"/listaProductos/"+result[i].codigo_lista+"/\">"+result[i].nombre_lista+"</a></th>");
						$("#tablePreview").append("<th scope='row'>"+ total_productos +"</th>");
						$("#tablePreview").append("<th scope='row'>"+productos_comprados+"</th>");
						$("#tablePreview").append("<th scope='row'>"+presupuestado+"</th>");
						$("#tablePreview").append("<th scope='row'>"+costo_real+"</th>");
						$("#tablePreview").append("<a class='btn btn-secondary' href=\"/agregarProductos/"+result[i].codigo_lista+"/\" role='button'>Comprar</a>");
						$("#tablePreview").append("</th>");
						$("#tablePreview").append("</tr>");
						$("#tablePreview").append("</tbody>");        
					}
				});
				 
			});
		}
	}); 
})
