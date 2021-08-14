from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256)
    num_pages = models.SmallIntegerField(
        default=0, verbose_name='No. Of Pages'
    )
    publish_date = models.DateField(auto_created=True, auto_now_add=True)
    isbn13 = models.CharField(max_length=13, blank=True)

    def __str__(self) -> str:
        return self.title
