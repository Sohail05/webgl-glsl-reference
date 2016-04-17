var $root = $('body');
 //.container >
$('a').click(function () {
    var href = $.attr(this, 'href');
    $root.animate({
        scrollTop: $(href).offset().top
    }, 500, function () {
        window.location.hash = href;

    });
    return false;
});

$(window).scroll(function () {
    if ($(this).scrollTop() > 500) {
        $('.totop').fadeIn();
    } else {
        $('.totop').fadeOut();
    }
});

$('.totop').click(function () {
    $root.animate({
        scrollTop: 0
    }, 800);
    return false;
});
