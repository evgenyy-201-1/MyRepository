from django.contrib import admin

from shop.models import Section, Product, Discount, Order, OrderLine

admin.site.register(Section)


# admin.site.register(Product)
# admin.site.register(Discount)
# admin.site.register(Order)
# admin.site.register(OrderLine)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'image', 'price', 'data', 'notice')
    # actions_on_bottom = True
    # actions_on_top = False
    list_per_page = 4
    search_fields = ('title', 'price')


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'value_percent')


class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'price', 'count')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'display_products',
        'discount', 'display_amount',
        'phone', 'email', 'address',
        'notice', 'date_order', 'data_send',
        'status'
    )
    fieldsets = (
        ('Информация о заказе', {
            'fields': ('need_delivery', 'discount')
        }),
        ('Информация о клиенте', {
            'fields': ('name', 'phone', 'email', 'address'),
            'description': 'Контактная информация'
        }),
        ('Доставка и оплата', {
            'fields': ('data_send', 'status')
        })
    )


admin.site.register(OrderLine, OrderLineAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Discount, DiscountAdmin)
