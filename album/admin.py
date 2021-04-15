from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Album)
class AlbumAdmin(ImportExportModelAdmin):
    list_display = ('title', 'theme', 'cover', 'paper', 'description')
    list_filter = ('cover', 'paper')
    search_fields = ('title__startswith',)
    pass


def in_progress(modeladmin, request, queryset):
    queryset.update(status='В процессе')


in_progress.short_description = "Изменить статус заказа 'В процессе'"


def completed(modeladmin, request, queryset):
    queryset.update(status='Выполнен')


completed.short_description = "Изменить статус заказа 'Выполнен'"


def canceled(modeladmin, request, queryset):
    queryset.update(status='Отменен')


canceled.short_description = "Изменить статус заказа 'Отменен'"


@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('id', 'album', 'size', 'package', 'user', 'date', 'price', 'description', 'status')
    search_fields = ('id__startswith',)
    actions = [in_progress, completed, canceled]
    pass


@admin.register(Buyer)
class UserAdmin(ImportExportModelAdmin):
    list_display = ('name', 'surname', 'number')
    search_fields = ('surname__startswith', 'number__startswith')
    pass


admin.site.register(Theme)
admin.site.register(Size)
admin.site.register(Cover)
admin.site.register(Paper)
admin.site.register(Package)
admin.site.register(Review)
admin.site.register(Message)
