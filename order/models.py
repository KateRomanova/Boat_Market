from django.db import models


class Order(models.Model):
    boat = models.ForeignKey('boat.Boat', on_delete=models.CASCADE, verbose_name='boat')

    name = models.CharField(max_length=150, verbose_name='name')
    email = models.EmailField(max_length=100, verbose_name='email')
    message = models.TextField()

    closed = models.BooleanField(default=False, verbose_name='order_is_closed')

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.boat} от {self.email}'

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
