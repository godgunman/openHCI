$(document).ready(function(){
	$(".chair .gallery img, .chair li").hover(function(){
		var order = $(this).attr('data-order');
		$("li[data-order='"+order+"']").addClass("hover");
		$("img[data-order='"+order+"']").addClass("hover");
	}, function(){
		var order = $(this).attr('data-order');
		$("li[data-order='"+order+"']").removeClass("hover");
		$("img[data-order='"+order+"']").removeClass("hover");
	});
});