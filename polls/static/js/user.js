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

function resetPhoto() {
	document.querySelector("input[type='file']#profile-photo").value = "";
	document.querySelector("img#photo-preview").src = document.querySelector("input[type='file']#profile-photo").dataset.default_picture;
}

function update(form) {
	let formdata = new FormData(form);
	formdata.append("reset_photo", document.querySelector("img#photo-preview").src.replace(window.location.origin, "") == document.querySelector("input[type='file']#profile-photo").dataset.default_picture);
	
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