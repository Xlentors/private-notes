from django.urls import path

from . import views

urlpatterns = [
    path("", views.note_list, name="note_list"),
    path("new/", views.note_create, name="note_create"),
    path("shared/<int:note_id>/", views.public_note_detail, name = "public_note_detail"),
    path("<int:note_id>/edit/", views.note_edit, name="note_edit"),
    path("<int:note_id>/delete/", views.note_delete, name="note_delete"),
    path("<int:note_id>/", views.note_detail, name="note_detail"),
]