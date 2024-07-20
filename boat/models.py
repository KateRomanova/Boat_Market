from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Owner(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя')
    email = models.EmailField(verbose_name='почта', unique=True)

    def __str__(self):
        return f'{self.email} ({self.name})'

    class Meta:
        verbose_name = 'владелец'
        verbose_name_plural = 'владельцы'


class Boat(models.Model):

    name = models.CharField(max_length=50, verbose_name='название')
    year = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='год выпуска')

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, verbose_name='владелец')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'лодка'
        verbose_name_plural = 'лодки'


class BoatHistory(models.Model):

    boat = models.ForeignKey(Boat, on_delete=models.CASCADE, verbose_name='лодка')
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, verbose_name='владелец', **NULLABLE)
    start_year = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='владел с')
    end_year = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='владел по')

    def __str__(self):
        return f'{self.boat.name} ({self.start_year}-{self.end_year})'

    class Meta:
        verbose_name = 'история'
        verbose_name_plural = 'история'
