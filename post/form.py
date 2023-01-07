from django import forms
from .models import Post


class CustomAddPostForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Title",
                "class": "form-control fields",
            }
        )
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Body",
                "class": "form-control fields",
            }
        )
    )

    class Meta:
        model = Post
        fields = ("title", "body")
