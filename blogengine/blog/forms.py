from django import forms
from django.core.exceptions import ValidationError

from .models import Tag, Post


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        ''' This function validate slug of a new tag '''
        new_slug = self.cleaned_data['title'].lower()

        if new_slug == 'create':
            raise ValidationError('Tag cannot be named "{}"'.format(new_slug))

        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('"{}" already exists'.format(new_slug))

        return new_slug


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

