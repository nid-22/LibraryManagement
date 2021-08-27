from django.contrib import admin
from django.db.models import fields


# Register your models here.
from .models import Books,Author
from Users.models import Users

class BookAdmin(admin.ModelAdmin):
    class meta:
        model = Books
        fields='__all__'

class AuthorAdmin(admin.ModelAdmin):
    class meta:
        model = Author
        fields='__all__'

class UsersAdmin(admin.ModelAdmin):
    class meta:
        model = Users
        fields = '__all__'

admin.site.register(Books,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Users,UsersAdmin)