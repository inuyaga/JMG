
from django.urls import path, include
from aplicaciones.tickets import views as tickets
app_name='tickets'
urlpatterns = [
    path('', tickets.InitTickets.as_view(), name='inicio'),
]