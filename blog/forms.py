from django import forms
from .models import Post, Comment
from .widgets import CustomClearableFileInput


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'slug': 'Slug',
            'author': 'Author',
            'preview': 'Preview',
            'section_one': 'Section 1',
            'section_two': 'Section 2',
            'section_three': 'Section 3',
            'image': 'Image',
            'source_link': 'Article Source Link',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'input-shadow'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
