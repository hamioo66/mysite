# -*- coding:UTF-8 -*-
from __future__ import unicode_literals

from django.db import models


class Catagory(models.Model):
    """博客分类"""
    name = models.CharField('名字', max_length=30)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    """博客标签"""
    tag_name = models.CharField('标签名', max_length=20, blank=True)
    create_time = models.DateTimeField('创建时间', auto_now=True)

    def __unicode__(self):
        return self.tag_name


class Author(models.Model):
    """博主"""
    name = models.CharField('博主姓名', max_length=30)
    email = models.EmailField('博主邮箱', blank=True)
    website = models.URLField('博主网站', blank=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class Blog(models.Model):
    """博客"""
    caption = models.CharField(max_length=50)
    describe = models.CharField(max_length=30, null=True)
    author = models.ForeignKey(Author)
    catagory = models.ForeignKey(Catagory, verbose_name='分类', null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publish_time',)

    def __unicode__(self):
        return u'%s %s %s %s' % (self.caption, self.describe, self.author, self.publish_time)


class Comment(models.Model):
    """评论"""
    blog = models.ForeignKey(Blog, verbose_name='博客')
    name = models.CharField('称呼', max_length=16)
    email = models.CharField('邮箱', max_length=16)
    content = models.CharField('内容', max_length=240)
    create = models.DateTimeField('发布时间', auto_now_add=True)

    def __unicode__(self):
        return self.content
