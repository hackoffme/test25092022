from django.urls import path

from singlpage import views

urlpatterns = [
    path('', views.OrdersView.as_view())
]