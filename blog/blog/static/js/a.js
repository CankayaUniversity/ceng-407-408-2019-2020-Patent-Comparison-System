(($) => {
    var now             = new Date;
    var day             = 864e5;
    var weeksToAdd      = 2;
    var tenWeeksFromNow = new Date(+now + day * 7 * weeksToAdd).toISOString().slice(0,10).replace(/\-/g, '/');
    $('[data-countdown-date].add-countdown-time').attr('data-countdown-date', tenWeeksFromNow);
  })(jQuery);