
from django.contrib import admin
from django.urls import path
from user.views import seeker_page, signup_page, login_page , home_page , logout_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup_page, name='signup'),
    path('', login_page, name='login'),
    path('home/', home_page, name='home'),
    path('seeker/', seeker_page, name='seeker'),
    path('logout/', logout_page, name='logout')
]
