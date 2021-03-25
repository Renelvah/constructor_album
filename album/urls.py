from django.conf.urls import url, include
from .views import AlbumViewset, BuyerViewset, OrderViewset, SizeViewset, CoverViewset, PatternViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('album', AlbumViewset, basename='album')
router.register('order', OrderViewset, basename='order')
router.register('buyer', BuyerViewset, basename='buyer')
router.register('size', SizeViewset, basename='size')
router.register('cover', CoverViewset, basename='cover')
router.register('pattern', PatternViewset, basename='pattern')

urlpatterns = [
    url('', include(router.urls)),


]