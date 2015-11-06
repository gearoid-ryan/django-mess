var main=function(){

    $('.description').hide();
    
    
    $('a.view').click(function(){
    
        if( $(this).text()==="Detailed View"){
        
        
        
            $('td.description').show();
            $('th.description').show();
            $(this).text("Summary View");
            
        } else{
        
            $('td.description').hide();
            $('th.description').hide();
            
            $(this).text("Detailed View");
            
        };
        
        
    
    
    });

    $('a.btn-success').click( function(){
    
        $('tbody').append("<tr><td>5</td><td>Swap5</td><td>1/1/2017</td><td>$1</td><td class=\"description\">Some stupid description</td></tr>");
        if( $('a.view').text()==="Detailed View"){
            $('td.description').hide();
        } else{
            $('th.description').show();
        };
            
    });
        
    $('a.btn-danger').click( function(){
       
        
        $('tbody tr:last').remove();
            
    });

};


$(document).ready(main);


