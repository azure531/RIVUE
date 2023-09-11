from django.contrib import admin
from django.urls import path, include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LandingPage, name='index'),
    path('show/', views.show_emp, name='show'),
    path('search/', views.search_product, name='search'),
    path('edit/<int:pk>', views.edit_emp, name='edit'),
    path('remove/<int:pk>', views.remove_emp, name='delete'),
    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('home/',views.imageupload,name='home'),
    path('success',views.success,name='success'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

