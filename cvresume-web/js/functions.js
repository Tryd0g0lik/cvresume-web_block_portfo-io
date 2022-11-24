 $(document).ready( function(){
      
       $("<div class='menu'></div>").prependTo('aside')
            
            
      
         
      
      
      $('#sidbar .menu').click(
               function(){
                    $('#sidbar > div > div').toggleClass('sidbar_mobile__chengeColor')
                    $('nav').toggleClass('sidbar_mobile__noactive');
               }
           )
     })