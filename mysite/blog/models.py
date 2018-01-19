# -*- coding:UTF-8 -*-
from __future__ import unicode_literals

from django.db import models


class Tag(models.Model):
    """博客类型"""
    tag_name = models.CharField(max_length=20, blank=True)
    create_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.tag_name


class Author(models.Model):
    """作者"""
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class Blog(models.Model):
    """博客"""
    caption = models.CharField(max_length=50)
    describe = models.CharField(max_length=30, null=True)
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publish_time',)

    def __unicode__(self):
        return u'%s %s %s %s' % (self.caption, self.describe, self.author, self.publish_time)
