from django import forms

from .models import Note, ChecklistItem

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "body", "is_public"]

class ChecklistItemForm(forms.ModelForm):
    class Meta:
        model = ChecklistItem
        fields = ["text"]