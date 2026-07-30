from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm
from .models import Note


def note_list(request):
    notes = Note.objects.all()
    
    return render(
        request,
        "notes/note_list.html",
        {"notes": notes}
    )
    
def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    
    return render(
        request,
        "notes/note_detail.html",
        {"note": note}
    )
    
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        
        if form.is_valid():
            note = form.save()
            
            return redirect("note_detail", note_id=note.id)
    else:
        form = NoteForm()
    
    return render(
        request,
        "notes/note_form.html",
        {
            "form": form,
            "page_title": "Create Note",    
        },
    )
    
def note_edit(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        
        if form.is_valid():
            note = form.save()
            
            return redirect("note_detail", note_id=note.id)
    else:
        form = NoteForm(instance=note)
    
    return render(
        request,
        "notes/note_form.html",
        {
            "form": form,
            "page_title": "Edit Note",
        },
    )
    
    
