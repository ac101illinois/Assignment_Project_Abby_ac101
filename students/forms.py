from django import forms
from students.models import Review
from students.models import Student
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "comment"]

    def clean_name(self):
        return self.cleaned_data["name"].strip()