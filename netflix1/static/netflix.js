$(function() {

  // Change background
  var backgroundImage = '/static/images/netflix-background.jpg';

  setInterval(function() {

    if (backgroundImage == '/static/images/netflix-background.jpg') {
      backgroundImage = '/static/images/netflix-background-2.jpg';
    } else {
      backgroundImage = '/static/images/netflix-background.jpg';
    }

    $('#background-image').css('background-image', 'url("' + backgroundImage  + '")');

  }, 6000);

  // Open & Close Menu
  $('.js-menu').click(function() {
	$('nav').toggleClass('open-menu');
  });

});