$(document).ready(function () {
    // set banner width
    var winHeight = window.innerHeight;
    $('#banner').height(winHeight - 150);

    // change skew degree when scrolling
    var $scrollLeft = $('.scroll-entry-left');
    var $scrollRight = $('.scroll-entry-right');
    $(window).scroll(function () {
        var top = document.documentElement.scrollTop
            || document.body.scrollTop;
        var percentage = 1 - Math.min(top / winHeight / 0.618, 1);
        var left = 'skewY(' + percentage * 15 + 'deg)';
        $scrollLeft.css({
            '-moz-transform': left,
            '-o-transform': left,
            '-ms-transform': left,
            '-webkit-transform': left,
            'transform': left,
            'opacity': percentage * 0.8
        });
        var right = 'skewY(-' + percentage * 15 + 'deg)';
        $scrollRight.css({
            '-moz-transform': right,
            '-o-transform': right,
            '-ms-transform': right,
            '-webkit-transform': right,
            'transform': right,
            'opacity': percentage * 0.8
        });
    });
});
