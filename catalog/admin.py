from django.contrib import admin

# Register your models here.

from .models import Author, Book, Genre, BookInstance

#admin.site.register (Book)
admin.site.register (Genre)
#admin.site.register (BookInstance)
#admin.site.register(Author)

#Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['last_name', 'first_name', ('date_of_birth', 'date_of_death')]

#Register the admin class with the associated model
admin.site.register (Author, AuthorAdmin)

# class BookInLine(admin.StackedInline):
#     model = Book
#Register the Admin classes for Book using the decorator
class BookInstanceInline(admin.TabularInline):
    model = BookInstance
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]
    # inlines = [BookInline]
#Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {'fields': ('book', 'imprint', 'id')}),
        ('Availability', {'fields': ('status', 'due_back')})
    )