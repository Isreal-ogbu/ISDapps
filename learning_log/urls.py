"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from learning_logs import views
from users import views as view
from django.contrib.auth.views import LoginView

urlpatterns = [

    path('', views.index, name='Home'),
    path('home/', views.index, name='Home'),
    path('topics/', views.Topics, name='Topic'),
    path('topics/<int:Topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:Entry_id>', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
    path('users/login/', LoginView.as_view(), {'template_name': 'registration/login.html'}, name='login'),
    path('users/logout/', view.Logout_views, name='logout'),
    path('users/register/', view.register, name='register'),
    path('admin/', admin.site.urls),
]
