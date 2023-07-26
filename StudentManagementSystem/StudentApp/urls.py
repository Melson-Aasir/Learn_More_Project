from django.urls import path

from StudentApp import views

urlpatterns = [
    path('', views.login_fun, name='log'),
    path('regdata', views.register, name='reg'),
    path('insert', views.insert, name='insert'),
    path('display', views.display, name='display'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='del'),
    path('home', views.home_fun, name='home'),
    path('course', views.course_fun, name='course'),
    path('insert-trainer', views.insert_trainer, name='insert_trainer'),
    path('display-trainer', views.display_trainer, name='display_trainer'),
    path('update-trainer/<int:id>', views.update_trainer, name='update_trainer'),
    path('delete-trainer/<int:id>', views.delete_trainer, name='del_trainer'),
    path('log_out', views.logout_fun, name='log_out')
]
