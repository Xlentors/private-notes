from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .forms import NoteForm
from .models import Note

@login_required
def note_list(request):
    notes = Note.objects.all()
    
    return render(
        request,
        "notes/note_list.html",
        {"notes": notes}
    )

@login_required
def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    
    return render(
        request,
        "notes/note_detail.html",
        {"note": note}
    )

@login_required
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

@login_required
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
    
@login_required
def note_delete(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    
    if request.method == "POST":
        note.delete()
        
        return redirect("note_list")
    
    return render(
        request,
        "notes/note_confirm_delete.html",
        {"note": note}
    )
        
    
    
    
