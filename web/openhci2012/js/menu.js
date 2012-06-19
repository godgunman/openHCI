$(function(){

    $("#btn1").css("background-color","#007DC3");

    function init(index) {
        for(i=1;i<=6;i++) {
            btn_str="#btn"+i
            $(btn_str).css("background-color","#595757");
        }
        btn_str="#btn"+index
        $(btn_str).css("background-color","#007DC3");
    }

    $("#btn1").click(function(){
   	$("#main_content").load("2012/index.html #main_content");
     init(1);
    });

    $("#btn2").click(function(){
   	$("#main_content").load("2012/intro.html #main_content"); 
     init(2);
    });

    $("#btn3").click(function(){
   	$("#main_content").load("2012/program.html #main_content");
     init(3);
    });

    $("#btn4").click(function(){
   	$("#main_content").load("2012/registration.html #main_content");
     init(4);
    });

    $(document).on('click', '#register_now', function(){
        $('#btn4').click();
    });
    //$("#register_now").click(function(){ $('#btn4').click(); });
    
    $("#btn5").click(function(){
   	$("#main_content").load("2012/passport.html #main_content");
     init(5);
    });

    $("#btn6").click(function(){
   	$("#main_content").load("2012/about.html #main_content");
     init(6);
    });

});
