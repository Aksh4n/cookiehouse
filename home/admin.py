from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(New)
admin.site.register(Post)
admin.site.register(Order)


