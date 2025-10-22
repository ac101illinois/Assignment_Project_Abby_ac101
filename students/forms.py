from django import forms
from students.models import Review
from students.models import Student
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"  # auto-create fields from model

    def clean_name(self):
        return self.cleaned_data["name"].strip()