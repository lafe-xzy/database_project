from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Campus)
admin.site.register(Cafeteria)
admin.site.register(ServedTime)
admin.site.register(Dish)
admin.site.register(Comments)