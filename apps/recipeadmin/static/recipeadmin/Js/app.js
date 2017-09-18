var ingredient;
var ing_count=1
function context_vars(obj){

        ingredient = JSON.parse(obj);

}
function new_qty(i, value){
  var qty_str="<input type='hidden' name='qty"+i+"'' value='"+value+"' >"
  return qty_str
}

function new_ing(i, value){
  var ing_str="</p><input type='hidden' name='igr"+i+"'' value='"+value+"' >"
  return ing_str
}


$(document).ready (function (){
  // x=new_ingredient(ing_count)
  // $(x[0]).insertAfter("p#ing")
  // $(x[1]).insertAfter("p#ing")

    console.log("Ready");
    $(document).on('click',"i#imore",function(){
      var curr_ing=$('#ing').val()
      var curr_qty=$('#qty').val()
      var i= new_ing(ing_count,curr_ing)
      var q= new_qty(ing_count,curr_qty)
      console.log(i)
      console.log(q)
      $(i).insertAfter("p#ingredient")
      $(q).insertAfter("p#ingredient")
      var str= curr_qty+" of "+ curr_ing
      $("div.inglist").append("<p>"+str+"</p>")
      ing_count++
      $('#ing').val("")
        $('#qty').val("")
    })

    $(document).on('click','button#create',function(){
      var curr_ing=$('#ing').val()
      var curr_qty=$('#qty').val()
      console.log(curr_ing.length)
      if (curr_ing.length>0&&curr_qty.length>0){
        var i= new_ing(ing_count,curr_ing)
        var q= new_qty(ing_count,curr_qty)
        $(i).insertAfter("p#ingredient")
        $(q).insertAfter("p#ingredient")
        $('#ing').remove()
        $('#qty').remove()
        $("#recipeform").submit()
      }
      else{
          $('#ing').remove()
          $('#qty').remove()
          $("#recipeform").submit()
      }


    })


})
