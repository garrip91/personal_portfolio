from django.db import models


# Create your models here.
class Project(models.Model):

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.CharField(max_length=250, verbose_name='Описание')
    image = models.ImageField(upload_to='portfolio/images/', verbose_name='Изображение')
    url = models.URLField(blank=True, verbose_name='Ссылка')
    
    def __str__(self):
        return self.title

    class Meta:
        #verbose_name = "Фильм"
        #verbose_name_plural = "Фильмы"
        ordering = ['title']