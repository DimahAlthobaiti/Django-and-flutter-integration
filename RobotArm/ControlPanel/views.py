from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Pose, Run
from .forms import PoseForm
from .serializers import PoseSerializer, RunSerializer


def run_values_view(request):
    latest_run = Run.objects.last()
    context = {
        'run': latest_run
    }
    return render(request, 'ControlPanel/Run.html', context)

def control_panel(request):
    poses = Pose.objects.all()

    action = request.POST.get("action")
    
    if request.method == 'POST':
        if action == "save":
            form = PoseForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("control_panel")

        elif action == "run":
            form = PoseForm(request.POST)
            if form.is_valid():
                Run.objects.create(
                motor1=form.cleaned_data['motor1'],
                motor2=form.cleaned_data['motor2'],
                motor3=form.cleaned_data['motor3'],
                motor4=form.cleaned_data['motor4'],
                status=1
)
                return redirect("run_display")

        elif action == "reset":
            form = PoseForm(initial={f'motor{i}': 90 for i in range(1, 5)})

        elif action == "load":
            pose_id = request.POST.get("load_id")
            pose = Pose.objects.get(id=pose_id)
            form = PoseForm(initial={
            'motor1': pose.motor1,
            'motor2': pose.motor2,
            'motor3': pose.motor3,
            'motor4': pose.motor4,
})

        elif action == "remove":
            pose_id = request.POST.get("remove_id")
            Pose.objects.filter(id=pose_id).delete()
            return redirect("control_panel")

    else:
        form = PoseForm(initial={f'motor{i}': 90 for i in range(1, 5)})

    return render(request, "ControlPanel/ControlPage.html", {"form": form, "poses": poses})

class PoseViewSet(viewsets.ModelViewSet):
    queryset = Pose.objects.all().order_by("id")
    serializer_class = PoseSerializer

class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all().order_by("-id")
    serializer_class = RunSerializer

    @action(detail=False, methods=["get"], url_path="latest")
    def latest(self, request):
        run = Run.objects.order_by("-id").first()
        if not run:
            return Response({"detail": "No runs yet."}, status=404)
        return Response(RunSerializer(run).data)