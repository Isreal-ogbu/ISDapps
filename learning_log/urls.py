from django.contrib import admin
from django.urls import path
from learning_logs import views
from users import views as view
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from learning_log import settings

urlpatterns = [

    path('', views.index, name='Home'),
    path('home/', views.index, name='Home'),
    path('topics/', views.Topics, name='Topic'),
    path('topics/<int:Topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:Entry_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('users/login/', LoginView.as_view(), {'template_name': 'registration/login.html'}, name='login'),
    path('users/logout/', view.Logout_views, name='logout'),
    path('users/register/', view.register, name='register'),
    path('admin/', admin.site.urls),
    path('query/', views.search, name='search'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
