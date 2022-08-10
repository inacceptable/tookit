$('document').ready(function() {
   $('#fullpage').fullpage({
						anchors: ['first_page', 'second_page', 'third_page'],
     					sectionsColor : ['#BD97CB', '#495C83', '#4D4C60'],
     					css3:true,
             		scrollingSpeed:1000,
						navigation:true,
						slidesNavigation:true,
						controlArrows:false,
						scrollbars:true,
						scrollOverflow:true,
						    scrollOverflowOptions: {
        scrollbars: false,
        preventDefault: false
    },

         });
   $(document).on('click', '#view-tools-button', function(){
  fullpage_api.moveTo('anchor-second_page', 1);
});
$(".tool-list-button").click(function(){
  $(".tool-list").slideToggle(300);
  $("#view-tools-svg" ).toggleClass("view-tools-svg_active");
  $(".tool-list-button" ).toggleClass("tool-list-button_active");
});

var windowsize = $(window).width();

$(window).resize(function() {
  var windowsize = $(window).width();
});

$(window).resize(function() {
  if ($(window).width() > 1000) {
      $(".tool-list").show();
  }
 else {
 
 }
});
setTimeout(function(){
    $.fn.fullpage.reBuild();
}, 100);
});

