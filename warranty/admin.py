from django.contrib import admin
from .models import ProductWarranty


@admin.register(ProductWarranty)
class ProductWarrantyAdmin(admin.ModelAdmin):
    list_display = (
        'serial_number',
        'model_name',
        'color',
        'status',
        'sale_date',
        'warranty_months',
        'warranty_end_display',
        'buyer_name',
        'channel',
    )
    list_filter = ('status', 'channel', 'model_name', 'sale_date')
    search_fields = ('serial_number', 'model_name', 'buyer_name', 'buyer_phone')
    readonly_fields = ('created_at', 'updated_at', 'warranty_end_display')
    fieldsets = (
        ('Товар', {
            'fields': ('serial_number', 'model_name', 'color', 'status')
        }),
        ('Гарантия', {
            'fields': ('sale_date', 'warranty_months', 'warranty_end_display')
        }),
        ('Покупатель', {
            'fields': ('buyer_name', 'buyer_phone', 'channel')
        }),
        ('Внутренние заметки', {
            'fields': ('notes', 'created_at', 'updated_at')
        }),
    )

    @admin.display(description='Гарантия до')
    def warranty_end_display(self, obj):
        return obj.warranty_end_date or '—'
