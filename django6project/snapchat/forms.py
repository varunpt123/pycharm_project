from django import forms

from snapchat.models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields='__all__'
