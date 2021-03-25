from .models import Album, Order, Buyer, Cover, Pattern, Size
from rest_framework import serializers

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ['id','title', 'size', 'cover', 'pages', 'pattern', 'description']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'number', 'price', 'album', 'buyer', 'date', 'status']


class BuyerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Buyer
        fields = ['id', 'name', 'surname', 'number']


class PatternSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pattern
        fields = ['id', 'pattern']


class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = ['id', 'size']


class CoverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cover
        fields = ['id', 'cover']
