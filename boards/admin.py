from django.contrib import admin

# Register your models here.
from .models import Boards,Lists,Cards

admin.site.register(Boards)
admin.site.register(Lists)
admin.site.register(Cards)
