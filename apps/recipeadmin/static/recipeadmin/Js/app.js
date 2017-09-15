var ingredient;

function context_vars(obj){

        ingredient = JSON.parse(obj);
        
}


$(document).ready (function (){
    $(document).on('click','p#test', function(){
        var d=$('recipeForm')
        console.log(d)
    // $.ajax({
    //     url: $(this).attr('action'),
    //     type: 'POST',
    //     contentType:'application/json',
    //     data: d,
    //     dataType: 'json'
    // })
    })
    console.log("Ready");
    $(document).on('click',"i#imore",function(){
    //      str="<input type='text' name='new_ingredient' ><i id='imore' class='fa fa-plus' aria-hidden='true'></i><br>" 
    //         +"<select name = 'Ingredient'>"     
    //     var name=""
    //     var id=""
    //    for(var i in ingredient){
    //       name = ingredient[i]["fields"]["Name"]
    //       id= ingredient[i]["fields"]["pk"]
    //     //    console.log(ingredient[i]["fields"]["Name"])
    //     str + " <option value ='"+ id+ "'>"+name+"</option>"
           
    //    }
 
    //     str+ "</select>"
           
        $(str).insertAfter("p#ing")
        
        console.log("imore")
    })

    
})