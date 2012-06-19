$(function(){
    $("#Intro-page").hide();
    $("#Program").hide();
    $("#Registration").hide();
    $("#Passport").hide();
    $("#AboutUs").hide();
});

$(function(){
    $("#btn1").click(function(){
        $("#home-page").animate({
            opacity: "1",
            width: "770px"/*,
            height: "40px",
            borderWidth: "5px",
            fontSize: "30px",
            marginTop: "40px",
            marginLeft: "20px"*/
        },1000);
        $("#Intro-page").animate({
            opacity: "0"
            //width: "0%"
        });
        $("#Program").animate({
            opacity: "0"
            //width: "0%"
        });
        $("#Registration").animate({
            opacity: "0"
            //width: "0%"
        });
        $("#Passport").animate({
            opacity: "0"
            //width: "0%"
        });
        $("#AboutUs").animate({
            opacity: "0"
            //width: "0%"
        });
    });

    $("#btn2").click(function(){
        $("#Intro-page").animate({
            opacity: "1",
            width: "770px"/*,
            height: "40px",
            borderWidth: "5px",
            fontSize: "30px",
            marginTop: "40px",
            marginLeft: "20px"*/
        },1000);
        $("#home-page").animate({
            opacity: "0"
            //width: "0%"
        });
        $("#Program").animate({
            opacity: "0"
            //width: "0%"
        });
        $("#Registration").animate({
            opacity: "0"
            //width: "0%"
        });
        $("#Passport").animate({
            opacity: "0"
            //width: "0%"
        });
        $("#AboutUs").animate({
            opacity: "0"
            //width: "0%"
        });
    });
    $("#btn3").click(function(){
        $("#Program").animate({
            opacity: "1",
            width: "80px"/*,
            height: "40px",
            borderWidth: "5px",
            fontSize: "30px",
            marginTop: "40px",
            marginLeft: "20px"*/
        },1000);
        $("#home-page").animate({
            opacity: "0"
            //width: "0%"
        });
        $("#Intro-page").animate({
            opacity: "0"
            //width: "0%"
        });
        $("#Registration").animate({
            opacity: "0"
            //width: "0%"
        });
        $("#Passport").animate({
            opacity: "0"
            //width: "0%"
        });
        $("#AboutUs").animate({
            opacity: "0"
            //width: "0%"
        });
    });
    $("#btn4").click(function(){
        $("#Registration").animate({
            opacity: "1",
            width: "80px"/*,
            height: "40px",
            borderWidth: "5px",
            fontSize: "30px",
            marginTop: "40px",
            marginLeft: "20px"*/
        },1000);
        $("#home-page").animate({
            opacity: "0"
            //width: "0%"
        });
        $("#Intro-page").animate({
            opacity: "0"
            //width: "0%"
        });
         $("#Program").animate({
            opacity: "0"
            //width: "0%"
        });
        $("#Passport").animate({
            opacity: "0"
            //width: "0%"
        });
        $("#AboutUs").animate({
            opacity: "0"
            //width: "0%"
        });
    });
    $("#btn5").click(function(){
        $("#Passport").animate({
            opacity: "1",
            width: "80px"/*,
            height: "40px",
            borderWidth: "5px",
            fontSize: "30px",
            marginTop: "40px",
            marginLeft: "20px"*/
        },1000);
        $("#home-page").animate({
            opacity: "0"
            //width: "0%"
        });
        $("#Intro-page").animate({
            opacity: "0"
            //width: "0%"
        });
         $("#Program").animate({
            opacity: "0"
            //width: "0%"
        });
        $("#Registration").animate({
            opacity: "0"
            //width: "0%"
        });
        $("#AboutUs").animate({
            opacity: "0"
            //width: "0%"
        });
    });
    $("#btn6").click(function(){
        $("#AboutUs").animate({
            opacity: "1",
            width: "80px"/*,
            height: "40px",
            borderWidth: "5px",
            fontSize: "30px",
            marginTop: "40px",
            marginLeft: "20px"*/
        },1000);
        $("#home-page").animate({
            opacity: "0"
            //width: "0%"
        });
        $("#Intro-page").animate({
            opacity: "0"
            //width: "0%"
        });
         $("#Program").animate({
            opacity: "0"
            //width: "0%"
        });
        $("#Registration").animate({
            opacity: "0"
            //width: "0%"
        });
        $("#Passport").animate({
            opacity: "0"
            //width: "0%"
        });
    });
});
