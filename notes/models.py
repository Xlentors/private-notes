from django.db import models
from django.conf import settings

# Create your models here.
class Note(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name = "notes",
    )

    title = models.CharField(max_length=200)
    body = models.TextField()
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            (
                "can_share_public_notes",
                "Can share notes publicly",
            ),
        ]

    def __str__(self):
        return self.title

class ChecklistItem(models.Model):
    note = models.ForeignKey(
        Note,
        on_delete=models.CASCADE,
        related_name="checklist_items"
    )

    text = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text