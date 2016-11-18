from rest_framework import serializers

from resume.models import *


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ("id", "title", "fa_string")


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ("id", "institution", "degree", "gpa", "start_date", "end_date", "is_current", "image",
                  "relevant_courses")


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ("id", "organization", "position", "start_date", "end_date", "is_current", "short_description")


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "title", "institution", "organization", "year", "skills", "short_description")


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ("id", "title", "conference", "co_authors", "link", "year")


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ("id", "what", "where", "short_description")
