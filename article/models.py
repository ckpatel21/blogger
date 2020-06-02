from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True , blank = True)
    text = models.CharField(max_length=500)
    desc = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.title