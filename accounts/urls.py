from django.urls import path, include
from rest_framework import routers
from accounts import views

router = routers.DefaultRouter()
router.register('category', views.CategoryViewSet)
router.register('tags', views.TagsViewSet)
router.register('blogpost', views.BlogPostViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('user-token/', views.UserTokenApi.as_view(), name='user-token'),


]