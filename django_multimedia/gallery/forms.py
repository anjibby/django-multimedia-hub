from django import forms
from .models import MediaItem

class MediaUploadForm(forms.ModelForm):
    class Meta:
        model = MediaItem
        fields = ['title', 'description', 'media_type', 'file', 'thumbnail']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'media_type': forms.Select(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),
        }