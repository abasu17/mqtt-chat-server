$( "#inputConfPassword" ).on("keyup",  function() {
	var pass = $("#inputPassword").val()
	if (pass == '')
		$("#inputPassword").css('border' , '1px solid red');
	else {
		var conf_pass = $( "#inputConfPassword" ).val()
		if (pass != conf_pass){
			$("#inputPassword").css('border' , '1px solid red');
			$("#inputConfPassword").css('border' , '1px solid red');
		} else {
			$("#inputPassword").css('border' , '1px solid green');
			$("#inputConfPassword").css('border' , '1px solid green');
		}
	}
}); 
