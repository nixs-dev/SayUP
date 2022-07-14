from rest_framework import serializers
from polls.models import User, Question, UserReport, QuestionReport, Punishment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'photo', 'username', 'gender')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class UserReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReport
        fields = '__all__'


class QuestionReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionReport
        fields = '__all__'


class PunishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Punishment
        fields = '__all__'