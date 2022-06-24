function send_friendrequest(user_id) {
    let cookie = document.cookie;
    let token = cookie.substring(cookie.indexOf("=") + 1);
    let status_icon = {
        'SENT': 'fas fa-user-clock',
        'SEND': 'fas fa-paper-plane'
    };
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
            let elem = document.querySelector('#friendRequestButton');
		    elem.querySelector('i').className = status_icon[result];
		}
    });
}

function accept_friendrequest(fr_id, accept) {
    let elem = document.querySelector('#friend-request-' + fr_id.toString());
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