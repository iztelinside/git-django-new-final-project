from django.db import models


class NewsHome(models.Model):
    title = models.CharField("Название",max_length=100)
    anons_content = models.TextField("Анонс", blank=True, max_length=200)
    full_content = models.TextField("Статья", blank=True, max_length=500)
    date = models.DateTimeField("Дата публикации")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural="Новости"
