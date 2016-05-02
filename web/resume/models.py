from __future__ import unicode_literals

from django.db import models


# Create your models here.
from django.utils import timezone


class BasicInfo(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return "%s - %s" % (self.key, self.value)


class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    gpa = models.CharField(max_length=20)
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")
    is_current = models.BooleanField(default=False)
    relevant_courses = models.TextField()

    def __str__(self):
        return "%s at %s" % (self.degree, self.institution)


class Experience(models.Model):
    organization = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")
    is_current = models.BooleanField(default=False)
    short_description = models.TextField()

    def __str__(self):
        return "%s at %s" % (self.position, self.organization)


class Publication(models.Model):
    YEARS = [(y, "%d" % y) for y in range(2010, 2090)]

    title = models.CharField(max_length=200)
    conference = models.CharField(max_length=200)
    co_authors = models.CharField(max_length=300)
    year = models.IntegerField(choices=YEARS, default=timezone.now().year)

    def __str__(self):
        return "%s... at %s... (%d)" % (
            self.title[:50], self.conference[:50], self.year)


class Skill(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Project(models.Model):
    YEARS = [(y, "%d" % y) for y in range(2010, 2090)]

    title = models.CharField(max_length=100)
    institution = models.ForeignKey(Education, blank=True, null=True)
    organization = models.ForeignKey(Experience, blank=True, null=True)
    year = models.IntegerField(choices=YEARS, default=timezone.now().year)
    skills = models.ManyToManyField(Skill, related_name='projects')
    short_description = models.TextField()

    def __str__(self):
        return "%s at %s" % (
            self.title, self.institution or self.organization or "leisure")


class Achievement(models.Model):
    short_description = models.CharField(max_length=200)
    where = models.CharField(max_length=100)
