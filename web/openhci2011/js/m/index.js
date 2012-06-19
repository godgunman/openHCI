$(document).ready(function(){
    $(".speakerInfo").each( function(index, element){
        var childrenCount = $(this).children().length;
        if (childrenCount==2) $(this).css({"padding-top": "12px"});
    });
    
    $(".datePanel").hide();
    $("#dateSelector a").click(function(){
        var panelID = "#date"+$(this).attr("id").substring(4, 6);
        $(".datePanel").slideUp();
        $(panelID).slideDown();
        $("#dateSelector a").removeClass("selected");
        $(this).addClass("selected");
    });

    var currentTime = new Date();
    var month = currentTime.getMonth()+1;
    var date = currentTime.getDate();
    var pureDate;
    if (month==7) {
        if (date>=4 && date<=8) pureDate = "7"+date;
        else pureDate = "74";
    } else pureDate = "74";
    $("#date"+pureDate).slideDown();
    $("#link"+pureDate).addClass("selected");
});
