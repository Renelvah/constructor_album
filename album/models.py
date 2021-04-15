from django.db import models


# Модель альбомов
class Album(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    theme = models.ForeignKey('Theme', on_delete=models.PROTECT)
    cover = models.ForeignKey('Cover', on_delete=models.PROTECT)
    paper = models.ForeignKey('Paper', on_delete=models.PROTECT)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


# Модель размеров
class Size(models.Model):
    TYPES = [
        ('horizontal', 'Горизонтальный'),
        ('vertical', 'Вертикальный'),
        ('square', 'Квадрат'),
    ]
    id = models.AutoField(primary_key=True)
    size = models.CharField(max_length=15)
    type = models.CharField(
        max_length=20,
        choices=TYPES,
        default='vertical',
    )

    def __str__(self):
        return f"{self.size} - {self.type}"


# Модель тематик
class Theme(models.Model):
    theme = models.CharField(max_length=100, db_index=True, default='Праздник')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.theme


# Модель обложек
class Cover(models.Model):
    id = models.AutoField(primary_key=True)
    cover = models.CharField(max_length=40)

    def __str__(self):
        return self.cover


# Модель типа бумаги
class Paper(models.Model):
    paper = models.CharField(max_length=40, db_index=True)

    def __str__(self):
        return self.paper


# Модель упаковок
class Package(models.Model):
    package = models.CharField(max_length=40, db_index=True)

    def __str__(self):
        return self.package


# Модель пользователей
class Buyer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    number = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.surname} {self.name}"


# Модель заказов
class Order(models.Model):
    STATUS = [
        ('in_progress', 'В процессе'),
        ('completed', 'Выполнен'),
        ('canceled', 'Отменен'),
    ]
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey('Album', on_delete=models.PROTECT)
    size = models.ForeignKey('Size', on_delete=models.PROTECT)
    package = models.ForeignKey('Package', on_delete=models.PROTECT, null=True, default=5)
    user = models.ForeignKey('Buyer', on_delete=models.CASCADE)
    date = models.DateTimeField()
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='in_progress',
    )

    def __str__(self):
        return f'{self.id}'


# Модель отзывов
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    date = models.DateTimeField()
    text = models.TextField(blank=True)

    def __str__(self):
        return self.id


# Модель сообщений
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    user = models.ForeignKey('Buyer', null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField()
    text = models.TextField(blank=True)

    def __str__(self):
        return self.id
