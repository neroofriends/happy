from django import forms
from .models import Pdf


class PdfForm(forms.ModelForm):
    class Meta:
        model = Pdf
        fields = ['title', 'uploader', 'address', 'tags']
        labels = {
            'title': '',
            'uploader': '',
            'address': '',
            'tags': ''
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input flex-grow'}),
            'uploader': forms.TextInput(attrs={'class': 'input flex-grow'}),
            'address': forms.URLInput(attrs={'class': 'input flex-grow'}),
            'tags': forms.TextInput(attrs={'class': 'input flex-grow',
                                           "placeholder": "biology, past papers, summary notes"}),
        }
