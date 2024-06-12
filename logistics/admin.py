
from django.contrib import admin
from rest_framework.exceptions import ValidationError

from logistics.models import SupplyChainParticipant, Product


@admin.register(SupplyChainParticipant)
class SupplyChainParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'supplier_link', 'debt')
    list_display_links = ('name', 'supplier_link')
    list_filter = ('city',)
    actions = ('clean_debt',)

    @admin.action(description="Обнулить задолженность выбранных объектов")
    def clean_debt(self, request, queryset):
        queryset.update(debt=0)

    @admin.display(description='Поставщик')
    def supplier_link(self, obj):
        return obj.supplier



@admin.register(Product)
class SupplyChainParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'date')
