from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test1@gmail.com", password="passs123"
        )
        cls.post = Post.objects.create(
            title="testpost", body="test 1 test2", author=cls.user
        )
        return super().setUpTestData()

    def test_post_model(self):
        self.assertEqual(self.post.title, "testpost")
        self.assertEqual(self.post.body, "test 1 test2")
        self.assertEqual(self.post.author.username, "testuser")

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/articles/1/detail/")
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test 1 test2")
        self.assertTemplateUsed(response, "home.html")
