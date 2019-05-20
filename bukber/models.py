from django.db import models
from django.utils import timezone


# Create your models here.
class Kelas(models.Model):
    nama = models.CharField(max_length=200)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self):
        if self.id:
            self.updated_at = timezone.now()
        else:
            self.updated_at = timezone.now()
            self.created_at = timezone.now()
        super().save()

    def __str__(self):
        return self.nama


class Peserta(models.Model):
    nama = models.CharField(max_length=200)
    kelas = models.ForeignKey('Kelas', on_delete=models.CASCADE)
    nominal = models.IntegerField()
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self):
        if self.id:
            self.updated_at = timezone.now()
        else:
            self.updated_at = timezone.now()
            self.created_at = timezone.now()
        super().save()

    def __str__(self):
        return self.nama
