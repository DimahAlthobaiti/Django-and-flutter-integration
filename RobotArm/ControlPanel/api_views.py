from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import Pose, Run
from .serializers import PoseSerializer, RunSerializer

class PoseViewSet(viewsets.ModelViewSet):
    queryset = Pose.objects.all().order_by("id")
    serializer_class = PoseSerializer

class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all().order_by("-created_at")
    serializer_class = RunSerializer

    @action(detail=False, methods=["get"], url_path="latest")
    def latest(self, request):
        run = Run.objects.order_by("-created_at").first()
        if not run:
            return Response({"detail": "No runs yet."}, status=status.HTTP_404_NOT_FOUND)
        return Response(RunSerializer(run).data)