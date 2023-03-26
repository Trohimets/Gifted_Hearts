from django.contrib import admin

from projects.models import Project, ProjectImage


class ProjectImageAdmin(admin.StackedInline):
    model = ProjectImage


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageAdmin]


admin.site.register(Project, ProjectAdmin)