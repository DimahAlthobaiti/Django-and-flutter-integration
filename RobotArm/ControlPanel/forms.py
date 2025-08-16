from django import forms
from .models import Pose

class PoseForm(forms.ModelForm):
    class Meta:
        model = Pose
        fields = ['motor1', 'motor2', 'motor3', 'motor4']
        widgets = {
            f'motor{i}': forms.NumberInput(attrs={
                'type': 'range', 'min': 0, 'max': 180, 'value': 90,
                'oninput': 'updateValue(this)'
            }) for i in range(1, 5)
        }