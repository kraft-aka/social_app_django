from django import forms

from  .models import Post
# from django.contrib.auth.forms import UserChangeForm


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    description = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}
    ))
    image = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={'class': 'form-control-file'}
    ))
    # tags = forms.ModelMultipleChoiceField(, widget=forms.SelectMultiple(
    #     attrs={'class': 'custom-select'}
    # ))

    class Meta:
        model = Post
        fields = ('title', 'description', 'image', 'tags')

