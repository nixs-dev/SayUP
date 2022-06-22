function send_friendrequest(user_id) {
    let cookie = document.cookie;
    let token = cookie.substring(cookie.indexOf("=") + 1);
    let data = new FormData();
    data.append("user_id", user_id);
    
    $.ajax({
        url: "/profiles/actions/sendfriendrequest",
        type: "POST",
        data: data,
        headers: {
            "X-CSRFToken": token
        },
		processData: false,
		contentType: false,
		success: function(result) {
		}
    });
}

function accept_friendrequest(elem, fr_id, accept) {
    //elem = elem.parent.parent;
    let cookie = document.cookie;
    let token = cookie.substring(cookie.indexOf("=") + 1);
    let data = new FormData();
    data.append("fr_id", fr_id);
    data.append("accept", accept);
    
    $.ajax({
        url: "/profiles/actions/acceptfriendrequest",
        type: "POST",
        data: data,
        headers: {
            "X-CSRFToken": token
        },
		processData: false,
		contentType: false,
		success: function(result) {
		    if(result) {
		        elem.remove();
		    }
		}
    });
}