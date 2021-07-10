$(document).ready(function () {

   // Footer Date
   $('#yearValue').text(new Date().getFullYear());

   // Mobile menu icon click
   $('.mobile-menu__nav-icon').click(function () {
      if ($(this).hasClass('open')) {
         $('.primary-mobile-nav, .secondary-mobile-nav, .tertiary-mobile-nav').removeClass('open');
         $('.primary-mobile-nav, .secondary-mobile-nav, .tertiary-mobile-nav').removeClass('closed-over');
         $('.mobile-menu-item-title').removeClass('visible');
         $(this).removeClass('open');
         $('.nlsg-c-navbar__inner__right-links li').not('.mobile-menu-container').fadeIn('fast');
      } else {
         $('.primary-mobile-nav').addClass('open');
         $(this).addClass('open');
      }
   });
});
