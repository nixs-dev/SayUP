from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from .models import User
from .models import FriendRequest
import json


def get_friendrequests(request):
    template = loader.get_template('polls/friend_requests_modal.html')
    
    requests_sent = FriendRequest.objects.filter(sender_id=request.session['user']['id'], accepted=False)
    requests_received = FriendRequest.objects.filter(recipient_id=request.session['user']['id'], accepted=False)
 
    context = {
        'requests_sent': requests_sent,
        'requests_received': requests_received
    }
    
    return template.render(context, request)

def send(request):
    user_id = request.POST['user_id']
    sender = User.objects.get(id=request.session['user']['id'])
    recipient = User.objects.get(id=user_id)
    status = ""
    
    friend_request_status_1 = FriendRequest.objects.filter(sender=sender, recipient=recipient).first()
    friend_request_status_2 = FriendRequest.objects.filter(sender=recipient, recipient=sender).first()
    matched_fr = None
    
    if friend_request_status_1 is not None:
        matched_fr = friend_request_status_1
    elif friend_request_status_2 is not None:
        matched_fr = friend_request_status_2
    else:
        matched_fr = None
    
    if matched_fr is None:
        FriendRequest(sender=sender, recipient=recipient).save()
        status = "SENT"
    else:
        matched_fr.delete()
        status = "SEND"
    
    return JsonResponse(status, safe=False)

def accept(request):
    fr_id = request.POST['fr_id']
    accept = json.loads(request.POST['accept'])
    friendrequest = FriendRequest.objects.get(id=fr_id)
    
    if accept:
        friendrequest.accepted = True
        friendrequest.save()
    else:
        friendrequest.delete()
    
    return JsonResponse(True, safe=False)