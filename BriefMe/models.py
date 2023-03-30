from django.db import models


class Brief(models.Model):
    title = models.CharField(
        max_length=500, blank=False, null=False, default='')
    description = models.TextField(blank=False, null=False, max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
