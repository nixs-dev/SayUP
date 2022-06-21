function send_friendrequest(user_id) {
    var cookie = document.cookie;
    var token = cookie.substring(cookie.indexOf("=") + 1);
    var data = new FormData();
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