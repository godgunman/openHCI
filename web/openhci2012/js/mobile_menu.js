
$(function(){

    $("#link72").css("background-color","#535353");
    $("#link72").css("color","#FFF");

    function init(index) {
        for(i=72;i<=77;i++) {
            btn_str="#link"+i
            $(btn_str).css("background-color","#FFFFFF");
            $(btn_str).css("color","#535353");
            $(btn_str).css("-webkit-border-radius","7px");
        }
        btn_str="#link"+index
        $(btn_str).css("background-color","#535353");
        $(btn_str).css("color","#FFF");
        $(btn_str).css("-webkit-border-radius","7px");


    }

    $("#link72").click(function(){
     init(72);
    });

    $("#link73").click(function(){
     init(73);
    });

    $("#link74").click(function(){
     init(74);
    });

    $("#link75").click(function(){
     init(75);
    });
    
    $("#link76").click(function(){
     init(76);
    });

    $("#link77").click(function(){
     init(77);
    });

});
