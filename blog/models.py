from django.db import models
from django.utils import timezone


class Post(models.Model):

    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, verbose_name='autor')
    title = models.CharField(max_length=200, verbose_name='tytuł')
    text = models.TextField(verbose_name='tekst')
    created_date = models.DateTimeField(
            default=timezone.now, verbose_name='data utworzenia')
    published_date = models.DateTimeField(
            blank=True, null=True, verbose_name='data_opublikowania')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posty'


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments', verbose_name='post')
    author = models.CharField(max_length=200, verbose_name='autor')
    text = models.TextField(verbose_name='tekst')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='data utworzenia')
    approved_comment = models.BooleanField(default=False, verbose_name='data_opublikowania')

    def approve(self):
        self.approved_comment = True
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Komentarz'
        verbose_name_plural = 'Komentarze'