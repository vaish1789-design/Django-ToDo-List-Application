from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("title", "description", "due_date")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. Prepare for interview"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Add a few details (optional)"}),
            "due_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if not title:
            raise forms.ValidationError("Please enter a task title.")
        return title
