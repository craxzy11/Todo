from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="home-page"),
    path('register/',views.register, name="register"),
    path('login/',views.loginpage, name="login"),
    path('/delete-task/<str:name>',views.deleteTodo, name="delete"),
    path('/update-task/<str:name>',views.updateTodo, name="update")
]


