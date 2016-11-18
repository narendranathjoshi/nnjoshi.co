from django.contrib import admin


# Register your models here.
from resume.models import *


class BasicInfoAdmin(admin.ModelAdmin):
    model = BasicInfo
    list_display = ("id", "key", "value")


class EducationAdmin(admin.ModelAdmin):
    model = Education
    list_display = (
        "id", "institution", "degree", "gpa", "start_date", "end_date",
        "is_current", "image")
    list_filter = (
        "institution", "degree", "gpa", "start_date", "end_date", "is_current")


class ExperienceAdmin(admin.ModelAdmin):
    model = Experience
    list_display = (
        "id", "organization", "position", "start_date", "end_date",
        "is_current")
    list_filter = (
        "organization", "position", "start_date", "end_date", "is_current")


class PublicationAdmin(admin.ModelAdmin):
    model = Publication
    list_display = ("id", "title", "conference", "link", "year")


class SkillAdmin(admin.ModelAdmin):
    model = Skill
    list_display = ("id", "title", "fa_string")


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = (
        "id", "title", "institution", "organization", "year")
    list_filter = ("title", "institution", "organization", "year")


class AchievementAdmin(admin.ModelAdmin):
    model = Achievement
    list_display = ("id", "what", "where", "short_description")


admin.site.register(BasicInfo, BasicInfoAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Achievement, AchievementAdmin)
