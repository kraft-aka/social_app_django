from django import forms

from tags.models import Tag


class TagForm(forms.ModelForm):
    title = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs= {'class':'form-control'}
        ))


    class Meta:
        model = Tag
        fields = ('title',)
        