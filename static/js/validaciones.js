$("#id_costo_presupuestado").keyup(function (){
    this.value = (this.value + '').replace(/[^0-9]/g, '');
   });

$("#id_costo_real").keyup(function (){
    this.value = (this.value + '').replace(/[^0-9]/g, '');
   });