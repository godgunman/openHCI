$(document).ready(function(){
    $(".speakerInfo").each( function(index, element){
        var childrenCount = $(this).children().length;
        if (childrenCount==2) $(this).css({"padding-top": "12px"});
    });
    
    $(".daySection").hide();
    $("#dateSelector a").click(function(){
        var panelID = "#date"+$(this).attr("id").substring(4, 6);
        $(".daySection").slideUp();
        $(panelID).slideDown();
        $("#dateSelector a").removeClass("selected");
        $(this).addClass("selected");
    });

    var currentTime = new Date();
    var month = currentTime.getMonth()+1;
    var date = currentTime.getDate();
    var pureDate;
    if (month==7) {
        if (date>=2 && date<=6) pureDate = "7"+date;
        else pureDate = "72";
    } else pureDate = "72";
    $("#date"+pureDate).slideDown();
    $("#link"+pureDate).addClass("selected");
});
