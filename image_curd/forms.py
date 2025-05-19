from django.forms import ModelForm
from .models import images


class imageForm(ModelForm):
    class Meta:
        model = images
