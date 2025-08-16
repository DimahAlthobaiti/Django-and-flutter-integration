from rest_framework import serializers
from .models import Pose, Run

class PoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pose
        fields = "__all__"

class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = "__all__"