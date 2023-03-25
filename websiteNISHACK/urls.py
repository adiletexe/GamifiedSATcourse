"""websiteNISHACK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from webapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('test/', views.test, name='test'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('payment/', views.payment, name='payment'),
    path('send_friend_request/<str:username>/', views.send_friend_request, name='send_friend_request'),
    path('accept_friend_request/<int:friendship_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('friends/', views.friends, name='friends_list'),
    path('satmath/', views.satmath, name='satmath'),
    path('satverbal/', views.satverbal, name='satverbal'),
    path('store/', views.store, name='store'),
    path('satverbaltest1', views.satverbaltest1, name='satverbaltest1'),
    path('satverbaltest2', views.satverbaltest2, name='satverbaltest2'),
    path('satmathtest1', views.satmathtest1, name='satmathtest1'),

#authentication
    path('signup/', views.signupsystem, name='signupsystem'),
    path('', views.loginsystem, name='loginsystem'),
    path('logout/', views.logoutsystem, name='logoutsystem'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)