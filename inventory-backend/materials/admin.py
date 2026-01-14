from django.contrib import admin
from .models import Material, Variant
# Register your models here.

class VariantInline(admin.TabularInline):
    model = Variant
    extra = 1

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    inlines = [VariantInline]
