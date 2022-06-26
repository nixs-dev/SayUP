function reload_all_polls(category) {
	$.ajax({
		url: "polls?" + (category ? "category=" + category : ""),
		type: "GET",
		processData: false,
		contentType: false,
		success: function(result){
			document.querySelector('.pollsContainer').innerHTML = result;
		}
	});
}

function save_poll() {
	form_data = new FormData();
	form_data.append("csrfmiddlewaretoken", document.getElementsByName("csrfmiddlewaretoken")[0].value);
	form_data.append("question", document.getElementById("new_question").value);
	form_data.append("category", document.getElementById("question_category").value);
	form_data.append("op1", document.getElementById("new_question_op1").value);
	form_data.append("op2", document.getElementById("new_question_op2").value);
	form_data.append("op3", document.getElementById("new_question_op3").value);
	form_data.append("op4", document.getElementById("new_question_op4").value);


	$.ajax({
		url: "save_poll",
		type: "POST",
		data: form_data,
		processData: false,
		contentType: false,
		success: function(result) {
			if(result == "OK") {
				alert("Enquete salva");
				reload_all_polls(null);
			}
			else {
				alert("Algo deu errado");
			}
		}
	});
}

function sendVote(form, option) {
    alert('oi');
	o = option.id;
	form.querySelector('#optionSelected').value = o;
	formdata = new FormData(form);
    alert('oi');
	$.ajax({
		url: "vote",
		type: "POST",
		data: formdata,
	    processData: false,
	    contentType: false,
		success: function(result) {
	    	reload_all_polls(null);
	 	}
	 });
}