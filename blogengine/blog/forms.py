from django import forms
from django.core.exceptions import ValidationError

from .models import Tag

class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['title', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug cannot be named "create" ')

        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('"{}" already exists'.format(new_slug))
        return new_slug
