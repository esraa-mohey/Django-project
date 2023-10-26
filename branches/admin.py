from django.contrib import admin

from .models import branch

@admin.register(branch)
class branchesAdmin (admin.ModelAdmin):
     list_display =['id','name']
