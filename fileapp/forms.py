from django import forms
from fileapp.models import UploadedFile
from django.contrib.auth.models import User

class FileUploadForm(forms.ModelForm):
    shared_with=forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    class Meta:
        model=UploadedFile
        fields=['file','shared_with']