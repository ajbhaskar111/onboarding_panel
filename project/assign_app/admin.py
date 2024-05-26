from django.contrib import admin
from .models import *

# Register your models here.
class Counter_show_table(admin.ModelAdmin):
    list_display = ['Name']


class User_show_table(admin.ModelAdmin):
    list_display = ["country_name", "User_name", "Email", "Password"]    


class Document_show_table(admin.ModelAdmin):
   
    list_display = ["Name_of_document","Country", "Has_backside", "OcrLables"]  


class Customer_show_table(admin.ModelAdmin):
    list_display = ["Surname", "Firstname", "Nationality", "Gender", "Card_number", "CreateBy"]  

class CustomerDocument_show_table(admin.ModelAdmin):
    list_display = ["Customer", "atteched_file", "Extracted_json", "Created_at"]     




admin.site.register(CountryModel,Counter_show_table)
admin.site.register(UserModel,User_show_table)
admin.site.register(DocumentSetModel,Document_show_table)
admin.site.register(CustomerMode,Customer_show_table)
admin.site.register(CustomerDocumentModel,CustomerDocument_show_table)


