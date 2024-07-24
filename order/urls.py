from django.urls import path

from order.apps import OrderConfig
from order.views import OrderCreateView

app_name = 'order'

urlpatterns = [
    path('create/<int:pk>', OrderCreateView.as_view(), name='create'),
]