from django.db import models


class Application(models.Model):
    SEMESTER_CHOICES = [
        ('не срочно', 'Не срочно'),
        ('срочно', 'Срочно'),
        ('очень срочно', 'Очень срочно'), ]

    title = models.CharField(max_length=225)
    text = models.TextField()
    date_create = models.DateField(auto_now_add=True)
    urgency = models.CharField(
        max_length=20,
        choices=SEMESTER_CHOICES,
        default='не срочно'
    )

    def __str__(self):
        return f'{self.title}'

class Files(models.Model):

    file = models.FileField(upload_to='application', blank=True, null=True, verbose_name='Файл')
    application = models.ForeignKey(Application, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Файлы"
        verbose_name_plural = "Файлы"

    def __str__(self):
        return self.file.name