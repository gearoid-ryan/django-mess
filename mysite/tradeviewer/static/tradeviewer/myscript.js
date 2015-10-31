var main=function(){

    $(document).keypress(function(event){
    
        if(event.which===65){
        

            $('tbody').append("<tr><td>5</td><td>Swap5</td><td>1/1/2017</td><td>$1</td></tr>");
            
        }
        else if(event.which===82){
        
            $('tbody tr#last').remove();
            
        };
         
        
    });

};


$(document).ready(main);