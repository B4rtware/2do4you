from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from todo.views import TodoDelete, TodoUpdate
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('impressum/', views.impressum, name="impressum"),
    path('contact/', views.contact, name="contact"),
    path('delete/<int:pk>/', TodoDelete.as_view(), name = "delete"),
    path('update/<int:pk>/', TodoUpdate.as_view(), name = "update"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)