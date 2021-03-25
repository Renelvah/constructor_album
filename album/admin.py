from django.contrib import admin
from .models import Album, Size, Cover, Pattern, Order, Buyer
from import_export.admin import ImportExportModelAdmin


@admin.register(Album)
class AlbumAdmin(ImportExportModelAdmin):
    list_display = ('title', 'size', 'cover', 'pages', 'pattern', 'description')
    list_filter = ("size", "pattern", )
    search_fields = ("title__startswith",)
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
    list_display = ('number', 'price', 'album', 'buyer', 'date', 'status')
    search_fields = ("number__startswith",)
    actions = [in_progress, completed, canceled]
    pass

@admin.register(Buyer)
class BuyerAdmin(ImportExportModelAdmin):
    list_display = ('name', 'surname', 'number')
    search_fields = ("surname__startswith",)
    pass

admin.site.register(Size)
admin.site.register(Cover)
admin.site.register(Pattern)