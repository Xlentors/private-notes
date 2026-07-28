from django.shortcuts import get_object_or_404, render

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
