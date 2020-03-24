from django.contrib import admin

# Register your models here.
from sewfinal.models import Category, SubCategory, SuperCategory, FabricDetails
from sewfinal.models import Components, Attributes, StyleDetails
from sewfinal.models import OrderDetails


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(SuperCategory)
admin.site.register(FabricDetails)
admin.site.register(Components)
admin.site.register(Attributes)
admin.site.register(StyleDetails)


admin.site.register(OrderDetails)


