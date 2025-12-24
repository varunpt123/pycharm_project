from django.contrib import admin

from snapchat.models import Student, Hospital, Books, Teacher


# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'genere', 'price')


admin.site.register(Books,BooksAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','mark', 'place')

admin.site.register(Student,StudentAdmin)

admin.site.register(Hospital)
admin.site.register(Teacher)
