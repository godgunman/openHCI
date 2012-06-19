$(document).ready(function(){
	newValue = $(".eventDay td:last-child").attr("rowspan")*2;
	$(".eventDay td:last-child").attr("rowspan", newValue);
	
	$(".program td:first-child").width($(".program").width()*0.15);
	$(".program td:nth-child(2)").width($(".program").width()*0.75);
	$(".program td:nth-child(3)").width($(".program").width()*0.1);
});