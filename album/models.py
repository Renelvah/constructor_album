from django.db import models

class Size(models.Model):
    size = models.CharField(max_length=10, db_index=True)
    def __str__(self):
        return self.size

class Cover(models.Model):
    cover = models.CharField(max_length=40, db_index=True)
    def __str__(self):
        return self.cover

class Pattern(models.Model):
    pattern = models.CharField(max_length=40, db_index=True)
    def __str__(self):
        return self.pattern

class Album(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    size = models.ForeignKey('Size', null=True, on_delete= models.PROTECT)
    cover = models.ForeignKey('Cover', null=True, on_delete= models.PROTECT)
    pages = models.IntegerField()
    pattern = models.ForeignKey('Pattern', null=True, on_delete= models.PROTECT)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.title

class Buyer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    number = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Order(models.Model):
    number = models.CharField(max_length=10)
    album = models.ForeignKey('Album', on_delete= models.PROTECT)
    buyer = models.ForeignKey('Buyer', on_delete= models.PROTECT)
    date = models.DateTimeField()
    price = models.IntegerField()
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.number