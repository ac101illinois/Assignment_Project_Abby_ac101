from django import forms

class ReviewForm(forms.Form):
    name = forms.CharField(max_length=50, label='Your Name')
    email = forms.EmailField(label='Email Address')
    shop = forms.CharField(label='Coffee Shop')
    rating = forms.IntegerField(min_value=1, max_value=5, label="Coffee Shop Rating",
                                widget=forms.NumberInput(attrs={'placeholder':'Enter your rating (1-5)'})
                                )
    review = forms.CharField(widget=forms.Textarea, label='Review')

    def clean_name(self):
        return self.cleaned_data["name"].strip()


class SearchShopForm(forms.Form):
    q = forms.CharField(label="Search Coffee Shops")