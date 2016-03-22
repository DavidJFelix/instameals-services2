from django.db import models

from .uuid import UUIDModelMixin


class Review(UUIDModelMixin, models.Model):
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    text = models.TextField(max_length=10000)
    rating = models.IntegerField(choices=RATING_CHOICES)
    posted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'instameals'

    def __str__(self):
        return "[{id}]: {rating}".format(
                id=str(self.id),
                rating=str(self.rating),
        )
