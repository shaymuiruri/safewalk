from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('panic-mode/', views.panic_mode, name='panic_mode'),
    # path('safe-route/', views.safe_route, name='safe_route'),
]
