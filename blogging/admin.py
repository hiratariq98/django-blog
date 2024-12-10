from django.contrib import admin

from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Post.categories.through
    extra = 1
    verbose_name = "Category"
    verbose_name_plural = "Categories"


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "author")
    search_fields = ("title", "author")
    list_filter = ("published_date", "author")

    inlines = (CategoryInline,)


class CategoryAdmin(admin.ModelAdmin):
    fields = ("name", "description")
    search_fields = ("name", "description")
    list_filter = ("name", "posts")
    exclude = ("posts",)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
