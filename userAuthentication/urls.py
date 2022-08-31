from django.urls import path


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout')
]
