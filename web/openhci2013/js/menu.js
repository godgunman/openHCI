$(function() {
    $("#head").css("background", "url(2013/images/head.png) no-repeat");
    $("#btn1").css("background", "url(2013/images/btn_01_on.png) no-repeat");
    var index = 1;
    init(1);

    $("a[id^=btn]").bind('mouseenter mouseleave', function(event) {
        var id = this.id.substring(3);
        switch (event.type) {
            case 'mouseenter':
                $(this).css("background", "url(2013/images/btn_0" + id + "_on.png) no-repeat");
                break;
            case 'mouseleave':
                if (id != index) {
                    $(this).css("background", "url(2013/images/btn_0" + id + ".png) no-repeat");
                }
                break;
        }
    });

    $("#btn1").click(function() {
        $("#main_content").load("2013/index.html #main_content");
        index = 1;
        init(1);
    });

    $("#btn2").click(function() {
        $("#main_content").load("2013/intro.html #main_content");
        index = 2;
        init(2);
    });

    $("#btn3").click(function() {
        $("#main_content").load("2013/program.html #main_content");
        index = 3;
        init(3);
    });

    $("#btn4").click(function() {
        $("#main_content").load("2013/registration.html #main_content");
        index = 4;
        init(4);
    });

    $(document).on('click', '#register_now', function() {
        $('#btn4').click();
    });
    //$("#register_now").click(function(){ $('#btn4').click(); });

    $("#btn5").click(function() {
        $("#main_content").load("2013/passport.html #main_content");
        index = 5;
        init(5);
    });

    $("#btn6").click(function() {
        $("#main_content").load("2013/about.html #main_content");
        index = 6;
        init(6);
    });
});

function init(id) {

    $("a[id^=btn]").each(function(i, element) {
        var id = this.id.substring(3);
        $(element).css("background", "url(2013/images/btn_0" + id + ".png) no-repeat");
    });

    $("#btn" + id).css("background", "url(2013/images/btn_0"+id+"_on.png) no-repeat");
}