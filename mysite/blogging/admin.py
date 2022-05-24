from django.contrib import admin

# Register your models here.
from blogging.models import Post, Category

# You will probably need to comment these out for the assignment:
# admin.site.register(Post)
# admin.site.register(Category)

class CategoryInline(admin.TabularInline):
    # model = Category
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # fields = ("title", "text", "author", "published_date")
    inlines = [CategoryInline]


# admin.site.register(Post, PostAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude= ("posts",)
    # fields = ("name", "description")



# admin.site.register(Category, CategoryAdmin)


