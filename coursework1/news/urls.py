from django.urls import path, include
from . import views
from rest_framework import routers
from django.http import HttpResponse
from django.contrib import admin

router = routers.DefaultRouter()
router.register('api/getstories', views.NewsStoryView)
router.register('api/getauthors', views.AuthorView)



urlpatterns = [ 
    # path('admin/', admin.site.urls),
    path('api/login/', views.HandleLogin),
    path('api/logout/', views.HandleLogout),
    path('api/poststory/', views.PostStory),
    path('api/getauthor/', views.GetAuthor),
    # path('api/getstories/', views.GetStories),
    path('api/deletestory/', views.DeleteStory),
    path('notloggedin/', views.LoginRedirect),
    # path('', views.PostStory)
    path('', include(router.urls))
]