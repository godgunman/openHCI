$(function() {
    $("#head").css("background", "url(2013/images/head.png) no-repeat");
    init(1);

    function init(index) {
        $("a[id^=btn][id!=btn" + index + "]").each(function(i, element) {
            var id = this.id.substring(3);
            $(element).css("background", "url(2013/images/btn_0" + id + ".png) no-repeat");
        });
        $("a[id^=btn][id!=btn" + index + "]").bind('mouseenter mouseleave', function(event) {
            var id = this.id.substring(3);
            switch (event.type) {
                case 'mouseenter':
                    $(this).css("background", "url(2013/images/btn_0" + id + "_on.png) no-repeat");
                    break;
                case 'mouseleave':
                    $(this).css("background", "url(2013/images/btn_0" + id + ".png) no-repeat");
                    break;
            }
        });
        btn_str = "#btn" + index;
        $(btn_str).css("background", "url(2013/images/btn_0" + index + "_on.png) no-repeat");
    }


    $("#btn1").click(function() {
        $("#main_content").load("index.html #main_content");
        init(1);
    });

    $("#btn2").click(function() {
        $("#main_content").load("intro.html #main_content");
        init(2);
    });

    $("#btn3").click(function() {
        $("#main_content").load("program.html #main_content");
        init(3);
    });

    $("#btn4").click(function() {
        $("#main_content").load("registration.html #main_content");
        init(4);
    });

    $(document).on('click', '#register_now', function() {
        $('#btn4').click();
    });
    //$("#register_now").click(function(){ $('#btn4').click(); });

    $("#btn5").click(function() {
        $("#main_content").load("passport.html #main_content");
        init(5);
    });

    $("#btn6").click(function() {
        $("#main_content").load("about.html #main_content");
        init(6);
    });

});
