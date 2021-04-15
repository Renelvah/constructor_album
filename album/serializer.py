from .models import *
from rest_framework import serializers


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'theme', 'cover', 'paper', 'description']


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ['id', 'theme', 'description']


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'size', 'pages']


class CoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cover
        fields = ['id', 'cover', 'color']


class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = ['id', 'paper']


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'package']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'album', 'size', 'package', 'user', 'date', 'price', 'description', 'status']


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ['id', 'name', 'surname', 'number']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'order', 'date', 'text']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'album', 'user', 'date', 'text']