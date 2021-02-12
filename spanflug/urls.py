"""spanflug URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from doc_app.views import WelcomeView, LoginView, LogutView, AddUserView, DashboardView, DocumentCreateView, \
    DocumentView, AttributesCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WelcomeView.as_view(), name='welcome'),
    path('login', LoginView.as_view(), name='login-view'),
    path('logout', LogutView.as_view(), name='logout-view'),
    path('register', AddUserView.as_view(), name='add-user-form'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('add-document', DocumentCreateView.as_view(), name='add-document'),
    path('document-view/<int:document_id>', DocumentView.as_view(), name='document-view'),
    path('add-attributes', AttributesCreateView.as_view(), name='add-attributes'),
]
