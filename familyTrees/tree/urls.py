
from django.urls import path
from.import views

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    # path('logout',views.logouts,name='logouts'),
    path('index',views.index,name='index'),
    path('form',views.form,name='form')

]