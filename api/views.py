from rest_framework import generics
from .models import Music
from polls.models import Question
from .serializers import MusicSerializer

# Create your views here.
class MusicList(generics.ListCreateAPIView):

    queryset = Question.objects.all()
    serializer_class = MusicSerializer
