from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout" ),
    path("add/", views.add_task, name="add"),
    path('update/<int:task_id>/', views.update_task_view, name="update"),
    path('task/<int:task_id>/compeleted', views.iscompleted, name="iscompleted"),
    path('delete/<int:task_id>/', views.delete_view, name="delete"),
    path('help/', views.helpview, name="help")
]
