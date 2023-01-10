from django import forms
from .models import Post, Comment


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


class CommentForm(forms.ModelForm):
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Comment here...",
                "class": "form-control fields",
            }
        )
    )

    class Meta:
        model = Comment
        fields = ("body",)
