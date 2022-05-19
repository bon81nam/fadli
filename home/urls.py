from django.urls import path
from .views import home, about, forms, activity, PEO, borang_akt
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('forms/', forms, name='forms'),
    path('activity/', activity, name='activity'),
    path('peo/', PEO, name='PEO'),
    path('cetak/', borang_akt, name='borang_akt'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout')
]
