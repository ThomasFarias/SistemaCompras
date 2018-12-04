$(document).ready(function(){
    $.ajax({url: "http://localhost:8000/back/tienda",  success: function(result){
       
        
        
    select = document.getElementById('id_tienda');

       
        $.each(result,function(i,items){  
            var opt = document.createElement('option');
            opt.value = result[i].codigo_tienda;
            opt.innerHTML =result[i].nombre_tienda;
            select.appendChild(opt);            
       });
    }});
})