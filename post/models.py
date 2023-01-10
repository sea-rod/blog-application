from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title.title()

    def get_absolute_url(self):
        return reverse("detail_post", kwargs={"pk": self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.body[:10]
