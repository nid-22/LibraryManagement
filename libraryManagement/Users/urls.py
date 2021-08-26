
from django.urls import path
from . import views as v


   
urlpatterns = [
    path('login', v.login, name="login"),
    path('home', v.home, name="home"),
    path('register',v.register, name="register"),
    path('logout',v.logout,name='logout'),

    path('updateUsers/<int:id>/',v.updateUsers,name='updateUsers'),
    path('deleteUsers/<int:id>/',v.deleteUsers,name='deleteUsers'),
    path('viewUsers',v.viewUsers,name='viewUsers')

    
]