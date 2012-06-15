$(document).ready(function(){
    window.addEventListener("load",function() {
      // Hide bar
      setTimeout(function(){ window.scrollTo(0, 1); }, 10);
    });

    $("#bookmark").hide().click(function(){
        $(this).fadeOut();
    });
    if (navigator.userAgent.search("iPhone")!=-1) {
        if (!window.navigator.standalone) {
            $("#bookmark").show();
        }
    }
});
