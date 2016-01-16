from rest_framework import serializers
from index.models import BlogEntry


class BlogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogEntry
        exclude = ["slug"]

