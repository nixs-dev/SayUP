var reset_photo = false;

function login(form) {
	let formdata = new FormData(form);

	$.ajax({
		url: "/auth/login/check",
		type: "POST",
		data: formdata,
	    processData: false,
	    contentType: false,
		success: function(result){
	    	if(result[0]) {
	    		window.location = '/home';
	    	}
	    	else {
	    		document.querySelector('.main-container').querySelector('form').querySelector('.error').innerHTML = result[1];
	    	}
	 	}
	 });
}

function update(form) {
	let formdata = new FormData(form);
	formdata.append("reset_photo", reset_photo);
	
	$.ajax({
		url: "/auth/profile/update",
		type: "POST",
		data: formdata,
	    processData: false,
	    contentType: false,
		success: function(result){
	    	if(result[0]) {
	    	    alert('b');
	    	}
	    	else {
	    	}
	 	}
	 });
}