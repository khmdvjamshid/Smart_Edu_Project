from django.contrib import admin
from . models import Course, Category, Tag

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "available","date")
    list_filter = ("available","category",)
    search_fields = ("name", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',) }

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',) }