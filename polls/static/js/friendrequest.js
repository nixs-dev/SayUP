var token;

document.cookie.split(";").forEach((c) => {
    let key = c.split("=")[0].trim();
    let value = c.split("=")[1].trim();
    
    if(key == "csrftoken") {
        token = value;
    }
});


function send_friendrequest(user_id) {
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
            let elem = document.querySelector('#friend-request-button');
		    elem.querySelector('i').className = status_icon[result];
		}
    });
}

function accept_friendrequest(elem, fr_id, accept) {
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