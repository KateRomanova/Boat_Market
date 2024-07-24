from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Owner(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя')
    email = models.EmailField(verbose_name='почта', unique=True)

    def __str__(self):
        return f'{self.email} ({self.name})'

    class Meta:
        verbose_name = 'owner'
        verbose_name_plural = 'owners'


class Boat(models.Model):

    name = models.CharField(max_length=50, verbose_name='name')
    year = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='made in (year)')

    price = models.IntegerField(**NULLABLE, verbose_name='price')

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name='owner')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'boat'
        verbose_name_plural = 'boats'


class BoatHistory(models.Model):

    boat = models.ForeignKey(Boat, on_delete=models.CASCADE, verbose_name='boat')
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, verbose_name='owner', **NULLABLE)
    start_year = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='owned from')
    end_year = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='owned till')

    def __str__(self):
        return f'{self.boat.name} ({self.start_year}-{self.end_year})'

    class Meta:
        verbose_name = 'history'
        verbose_name_plural = 'history'
