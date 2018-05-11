from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

from todo.views import TodoDeleteView, TodoUpdateView, TodoSignupView, TodoCreateView, TodoIndexView
from . import views
from . import forms

urlpatterns = [
    path('', TodoIndexView.as_view() , name="index"),
    path('accounts/login', LoginView.as_view(authentication_form = forms.TodoAuthenticationForm), name = "login"),
    path('accounts/signup', TodoSignupView.as_view(), name = "signup"),
    path('create/', TodoCreateView.as_view(), name="create"),
    path('impressum/', views.impressum, name="impressum"),
    path('contact/', views.contact, name="contact"),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name = "delete"),
    path('update/<int:pk>/', TodoUpdateView.as_view(), name = "update"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)