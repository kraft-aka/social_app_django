from django.db import models

from django.urls import reverse


class Tag(models.Model):
    title = models.CharField(max_length=255, db_index=True)

    class Meta:
        ordering = ('-id',)

    def get_absolute_url(self):
        return reverse('tag-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title