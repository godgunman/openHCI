$(document).ready(function(){
	//var galleryWidth = $("#gallery").width();
	//Galleria.loadTheme('/css/galleria/classic/galleria.classic.js');
	//$("#gallery").galleria({ width: galleryWidth, height: 500 });
	
	// Feature Item
	$(".featureItem").height($(".featureItem").width()*0.6);
	$(".fullImage").height($(".fullImage").width()*0.6);
	
	// Show map
	var latlng = new google.maps.LatLng(25.01956, 121.54159);
	var myOptions = {
			zoom: 14,
			center: latlng,
			mapTypeId: google.maps.MapTypeId.ROADMAP,
			
	};
	var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
	// Add marker
	var marker = new google.maps.Marker({
	      position: latlng, 
	      map: map,
	      title: "NTU CSIE"
	  });
	// Click marker
	google.maps.event.addListener(marker, 'click', function() {
		window.open("http://maps.google.com/?q=%E5%8F%B0%E5%A4%A7%E8%B3%87%E5%B7%A5%E7%B3%BB@25.01956,121.54159");
	});
	
	// Hover
	$(".featureItem").hover(function(){
		$(this).addClass("hover");
		originalPath = $("img", this).attr("src");
		newPath = originalPath.substring(0, originalPath.length-9)+".png"
		$("img", this).attr("src", newPath);
	}, function(){
		$(this).removeClass("hover");
		originalPath = $("img", this).attr("src");
		newPath = originalPath.substring(0, originalPath.length-4)+"_pale.png"
		$("img", this).attr("src", newPath);
	});
});
