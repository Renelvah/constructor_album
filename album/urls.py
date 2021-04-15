from django.conf.urls import url, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('album', AlbumViewset, basename='album')
router.register('theme', ThemeViewset, basename='theme')
router.register('size', SizeViewset, basename='size')
router.register('cover', CoverViewset, basename='cover')
router.register('paper', PaperViewset, basename='paper')
router.register('package', PackageViewset, basename='package')
router.register('order', OrderViewset, basename='order')
router.register('buyer', BuyerViewset, basename='user')
router.register('review', ReviewViewset, basename='review')
router.register('message', MessageViewset, basename='message')

urlpatterns = [
    url('', include(router.urls)),
]
