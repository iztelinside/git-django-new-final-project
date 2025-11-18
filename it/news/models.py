from django.db import models


class NewsHome(models.Model):
    title = models.CharField("We are the champions",max_length=100)
    anons_content = models.TextField("Text Content", blank=True, max_length=200)
    full_content = models.TextField("Full Content", blank=True, max_length=500)
    date = models.DateTimeField("Date and Time")

    def __str__(self):
        return self.title
