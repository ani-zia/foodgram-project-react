from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Tag name')
    color = models.CharField(max_length=50, unique=True, verbose_name='HEX Color')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    
    def __str__(self):
        return f'{self.name}'