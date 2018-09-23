from django.urls import path
from . import views
urlpatterns = [
    path('', views.MainView, name='home'),
    path('htmlclasswork/hollywoods',views.Hollyview, name='hollywoodpage'),
    path('htmlclasswork/bollywood',views.Bollyview, name='bollywoodpage'),
    path('htmlclasswork/cartoon',views.Cartoonview, name='cartoonpage'),
]
