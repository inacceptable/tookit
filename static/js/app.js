$('document').ready(function() {
   $('#fullpage').fullpage({
						anchors: ['first_page', 'second_page', 'third_page'],
     				sectionsColor : ['#BD97CB', '#495C83', '#4D4C60'],
     					  // Navigation
  menu: '#menu',
  lockAnchors: false,
  anchors:['firstPage', 'secondPage'],
  navigation: false,
  navigationPosition: 'right',
  navigationTooltips: ['first_page', 'second_page', 'third_page'],
  showActiveTooltip: false,
  slidesNavigation: false,
  slidesNavPosition: 'bottom',

  // Scrolling
  css3: true,
  scrollingSpeed: 700,
  autoScrolling: true,
  fitToSection: true,
  scrollBar: false,
  easing: 'easeInOutCubic',
  easingcss3: 'ease',
  loopBottom: false,
  loopTop: false,
  loopHorizontal: true,
  continuousVertical: false,
  continuousHorizontal: false,
  scrollHorizontally: false,
  interlockedSlides: false,
  dragAndMove: false,
  offsetSections: false,
  resetSliders: false,
  fadingEffect: false,
  scrollOverflow: true,
  scrollOverflowMacStyle: false,
  scrollOverflowReset: false,
  touchSensitivity: 15,
  bigSectionsDestination: null,

  // Accessibility
  keyboardScrolling: true,
  animateAnchor: true,
  recordHistory: true,

  // Design
  controlArrows: true,
  controlArrowsHTML: [
    '<div class="fp-arrow"></div>', 
    '<div class="fp-arrow"></div>'
  ],
  verticalCentered: true,
  paddingTop: '3em',
  paddingBottom: '10px',
  responsiveWidth: 0,
  responsiveHeight: 0,
  responsiveSlides: false,
  parallax: false,
  parallaxOptions: {type: 'reveal', percentage: 62, property: 'translate'},
  dropEffect: false,
  dropEffectOptions: { speed: 2300, color: '#F82F4D', zIndex: 9999},
  waterEffect: false,
  waterEffectOptions: { animateContent: true, animateOnMouseMove: true},
  cards: false,
  cardsOptions: {perspective: 100, fadeContent: true, fadeBackground: true},

  // Custom selectors
  sectionSelector: '.section',
  slideSelector: '.slide',

  lazyLoading: true,
  observer: true,
  credits: { enabled: true, label: 'Made with fullPage.js', position: 'right'},

  // Events
  beforeLeave: function(origin, destination, direction, trigger){},
  onLeave: function(origin, destination, direction, trigger){},
  afterLoad: function(origin, destination, direction, trigger){},
  afterRender: function(){},
  afterResize: function(width, height){},
  afterReBuild: function(){},
  afterResponsive: function(isResponsive){},
  afterSlideLoad: function(section, origin, destination, direction, trigger){},
  onSlideLeave: function(section, origin, destination, direction, trigger){},
  onScrollOverflow: function(section, slide, position, direction){}
// even though this is set to true, it's not working

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

