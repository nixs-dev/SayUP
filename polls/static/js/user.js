function login(form) {
	formdata = new FormData(form);

	$.ajax({
		url: "login/check",
		type: "POST",
		data: formdata,
	    processData: false,
	    contentType: false,
		success: function(result){
	    	if(result[0]) {
	    		window.location = '/';
	    	}
	    	else {
	    		document.querySelector('.mainContainer').querySelector('form').querySelector('.error').innerHTML = result[1];
	    	}
	 	}
	 });
}