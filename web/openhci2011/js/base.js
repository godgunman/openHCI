$(document).ready(function(){
	// Nav bar
	var navItemTarget = null;
	currentPath = window.location.pathname;
	if (currentPath.search("/about/")!=-1)
		navItemTarget = $("#navAbout");
	else if (currentPath.search("/program/")!=-1)
		navItemTarget = $("#navProgram");
	else if (currentPath.search("/introAndGoals/")!=-1)
		navItemTarget = $("#navIntroAndGoals");
	else if (currentPath.search("/registration/")!=-1)
		navItemTarget = $("#navRegistration");
        else if (currentPath.search("/passport/")!=-1)
                navItemTarget = $("#navPassport");
        else if (currentPath.search("/final/")!=-1)
                navItemTarget = $("#navFinal");
	else if (currentPath.search("/")!=-1)
		navItemTarget = $("#navMain");
	if (navItemTarget) navItemTarget.addClass("selected");
	$("#siteName").click(function(){
		window.location="/";
	});
	
	// Add hover style
	$("footer, header, a.navItem, button").hover(function(){
		$(this).addClass("hover");
	}, function(){
		$(this).removeClass("hover");
	});
	
	$("#browserHint").hide();
	if (navigator.userAgent.search("WebKit")==-1) {
		$("#browserHint").show();
	}
	
	$("table tr:odd").addClass("odd");
	$("table tr:even").addClass("even");
});
