from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Note

class NoteAccessTests(TestCase):
    def setUp(self):
        User = get_user_model()

        self.user_one = User.objects.create_user(
            username="user_one",
            password="test-password",
        )

        self.user_two = User.objects.create_user(
            username="user_two",
            password="test-password",
        )

        self.note_one = Note.objects.create(
            owner=self.user_one,
            title="User One Note",
            body="Test note of user one.",
        )

        self.note_two = Note.objects.create(
            owner=self.user_two,
            title="User Two Note",
            body="Test note of user two..",
        )

    def test_logged_out_user_is_redirected_from_note_list(self):
        response = self.client.get(reverse("note_list"))

        expected_url = f"{reverse('login')}?next={reverse('note_list')}"

        self.assertRedirects(response, expected_url)

    def test_user_sees_only_their_own_notes(self):
        self.client.login(
            username="user_one",
            password="test-password",
        )

        response = self.client.get(reverse("note_list"))
        notes = response.context["notes"]

        self.assertIn(self.note_one, notes)
        self.assertNotIn(self.note_two, notes)

    def test_user_cannot_access_or_modify_another_users_note(self):
        self.client.login(
            username = "user_one",
            password = "test-password",
        )

        detail_url = reverse("note_detail", args=[self.note_two.id])
        edit_url = reverse("note_edit", args=[self.note_two.id])
        delete_url = reverse("note_delete", args=[self.note_two.id])

        detail_response = self.client.get(detail_url)
        edit_response = self.client.get(edit_url)
        delete_response = self.client.post(delete_url)

        self.assertEqual(detail_response.status_code, 404)
        self.assertEqual(edit_response.status_code, 404)
        self.assertEqual(delete_response.status_code, 404)

        note_still_exists = Note.objects.filter(id=self.note_two.id).exists()
        self.assertTrue(note_still_exists)

    def test_public_note_is_viewable_while_logged_out(self):
        self.note_one.is_public = True
        self.note_one.save()

        public_url = reverse(
            "public_note_detail",
            args=[self.note_one.id],
        )

        response = self.client.get(public_url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.note_one.title)

    def test_private_note_is_not_viewable_through_public_url(self):
        public_url = reverse(
            "public_note_detail",
            args=[self.note_one.id],
        )

        response = self.client.get(public_url)

        self.assertEqual(response.status_code, 404)