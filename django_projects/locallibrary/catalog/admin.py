from django.contrib import admin

# Register your models here.

from catalog.models import Author, Genre, Language, Book, BookInstance

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
#admin.site.register(BookInstance)

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


# Enable to add associated records at the same time. For e.g here to have book info and info about specific copies youve got on the same detail page
#Use of inlines of type TabularInLine(horizontal layout) or StackedInLine(vertical layout)
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    #this part removes the extra fields
    extra = 0

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
#this is related the BooksInstanceInline class
    inlines = [BooksInstanceInline]




# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
