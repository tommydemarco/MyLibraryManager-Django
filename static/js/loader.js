
  //JQUERY LOEAD FUNCTION
  jQuery(window).on("load", function() {
     
      function handlePreloader() {
          var preloader = $('.preloader');
          if(preloader.length){
          preloader.delay(600).fadeOut(800);
          }
      }
      handlePreloader(); 
  });
