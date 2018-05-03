from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from todo.views import TodoDelete
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('delete/<int:pk>/', TodoDelete.as_view(), name = "delete"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)