from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    chapter = models.IntegerField()
    lesson_number = models.FloatField()
    description = models.TextField()
    video = models.TextField()
    worksheet = models.TextField()
    answerkey = models.TextField()
    slug = models.SlugField(default='')

    objects = models.Manager()

    def __str__(self):
        return self.title
