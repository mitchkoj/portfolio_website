from django.contrib import admin
from .models import Project

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    action_on_top = True
    actions_on_bottom = False

    fields = ('title', 'description', 'technology', 'image')
