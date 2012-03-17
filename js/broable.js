$(document).ready(function(){
    $("form#submit").submit(function(){
	$("h2#response").text("");
	$.ajax({
	    url : "/broable",
	    data : {"q" : $("input#q").val()},
	    success : function(data){
		$("h2#response").text(data);
		if (data == "Fuck yea")
		    $("h2#response").css({"color" : "green"});
		else
		    $("h2#response").css({"color" : "red"});
	    }
	});
	return false;
    });
    
    $("input#q").focus(function(){
	$("h2#response").text("");
    });
    
    $("input#q").blur(function(){
	$("h2#response").text("");
    });
});
