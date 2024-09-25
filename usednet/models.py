from django.db import models

from django.db import models
from django.utils import timezone

class Content(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag', related_name='contents')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Branch(models.Model):
    content = models.ForeignKey(Content, related_name='branches', on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey('self', related_name='responses', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    url = models.URLField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

