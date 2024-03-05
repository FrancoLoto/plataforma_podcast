from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.text import slugify

ALLOWED_EXTENSIONS = ["flac", "ogg", "mp3", "wav"]


class Podcast(models.Model):
    title = models.CharField(verbose_name="Título", max_length=1000)
    description = models.TextField(
        verbose_name="Descripción", max_length=10000)
    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, verbose_name="Autor")
    slug = models.SlugField(verbose_name="Slug",
                            max_length=1000,
                            unique=True,
                            editable=False
                            )
    file = models.FileField(verbose_name="Podcast Archivo",
                            upload_to="podcast_uploads",
                            validators=[
                                FileExtensionValidator(
                                    allowed_extensions=ALLOWED_EXTENSIONS
                                )
                            ])
    thumbnail = models.ImageField(verbose_name="Podcast Thumbnail",
                                  upload_to="podcast_thumbnails"
                                  )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Podcast, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} by {self.author.username}'
