from django.contrib import admin
from.models import Property,PropertyImages,Place,Category,PropertyReview,PropertyBook
# Register your models here.
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportModelAdmin
# Apply summernote to all TextField in model.


# class Property_A(admin.StackedInline):
#     model = Property 
#     extra = 1

class Property_Images(admin.TabularInline):
    model = PropertyImages 
    extra = 1
    
    
class Property_Admin(admin.ModelAdmin):
    inlines=[Property_Images]
    
class SomeModelAdmin(SummernoteModelAdmin,Property_Admin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display=['name','price','len_commnets','get_avg_rating','check_vailability']
class ProductImportExportModelAdmin(ImportExportModelAdmin):
    pass
class productAdminn(ProductImportExportModelAdmin):
    pass

class PropertyBookAdmin(admin.ModelAdmin):
    list_display =['user','property','in_progress']
admin.site.register(Property,SomeModelAdmin,)
admin.site.register(PropertyImages)
admin.site.register(Place,productAdminn)
admin.site.register(Category)
admin.site.register(PropertyReview)
admin.site.register(PropertyBook,PropertyBookAdmin)
