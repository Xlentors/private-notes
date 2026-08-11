from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .forms import NoteForm, ChecklistItemForm
from .models import Note, ChecklistItem

@login_required
def note_list(request):
    notes = Note.objects.filter(owner=request.user)

    return render(
        request,
        "notes/note_list.html",
        {"notes": notes}
    )

@login_required
def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id, owner=request.user)
    checklist_form = ChecklistItemForm()

    return render(
        request,
        "notes/note_detail.html",
        {
            "note": note,
            "checklist_form": checklist_form,
        }
    )

@login_required
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()

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
    note = get_object_or_404(Note, id=note_id, owner=request.user)

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
    note = get_object_or_404(Note, id=note_id, owner=request.user)

    if request.method == "POST":
        note.delete()

        return redirect("note_list")

    return render(
        request,
        "notes/note_confirm_delete.html",
        {"note": note}
    )

def public_note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id, is_public=True)

    return render(
        request,
        "notes/public_note_detail.html",
        {"note": note}
    )


@login_required
@require_POST
def checklist_item_create(request, note_id):
    note = get_object_or_404(Note, id = note_id, owner = request.user)

    form = ChecklistItemForm(request.POST)

    if form.is_valid():
        checklist_item = form.save(commit=False)
        checklist_item.note = note
        checklist_item.save()

    return redirect("note_detail", note_id=note.id)

@login_required
@require_POST
def checklist_item_toggle(request, item_id):
    checklist_item = get_object_or_404(ChecklistItem, id = item_id, note__owner=request.user)
    checklist_item.is_completed = not checklist_item.is_completed
    checklist_item.save()

    return redirect("note_detail", note_id=checklist_item.note.id)

@login_required
@require_POST
def checklist_item_delete(request, item_id):
    checklist_item = get_object_or_404(ChecklistItem, id = item_id, note__owner=request.user)
    note_id = checklist_item.note.id
    checklist_item.delete()

    return redirect("note_detail", note_id = note_id)