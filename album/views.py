from django.shortcuts import render
from rest_framework import viewsets
from .serializer import *
from .models import *


class AlbumViewset(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        album = Album.objects.all()
        return album


class OrderViewset(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        order = Order.objects.all()
        return order


class BuyerViewset(viewsets.ModelViewSet):
    serializer_class = BuyerSerializer

    def get_queryset(self):
        user = Buyer.objects.all()
        return user


class CoverViewset(viewsets.ModelViewSet):
    serializer_class = CoverSerializer

    def get_queryset(self):
        cover = Cover.objects.all()
        return cover


class SizeViewset(viewsets.ModelViewSet):
    serializer_class = SizeSerializer

    def get_queryset(self):
        size = Size.objects.all()
        return size


class PaperViewset(viewsets.ModelViewSet):
    serializer_class = PaperSerializer

    def get_queryset(self):
        paper = Paper.objects.all()
        return paper


class PackageViewset(viewsets.ModelViewSet):
    serializer_class = PackageSerializer

    def get_queryset(self):
        package = Package.objects.all()
        return package


class ThemeViewset(viewsets.ModelViewSet):
    serializer_class = ThemeSerializer

    def get_queryset(self):
        theme = Theme.objects.all()
        return theme


class MessageViewset(viewsets.ModelViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
        message = Message.objects.all()
        return message


class ReviewViewset(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        review = Review.objects.all()
        return review
