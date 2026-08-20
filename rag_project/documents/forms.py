from django import forms
from .models import Document
class Documentform(forms.ModelForm):
    class Meta:
        model=Document
        fields=["title","file"]
    def clean_file(self):
        file = self.cleaned_data["file"]

        if not file.name.lower().endswith(".pdf"):
            raise forms.ValidationError(
                "Only PDF files are allowed."
            )

        return file        
