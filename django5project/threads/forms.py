from django import forms

from threads.models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields='__all__'