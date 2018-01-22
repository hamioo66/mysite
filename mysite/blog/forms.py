# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/1/22
describle:博客的评论
"""
from django import forms
class CommentForm(forms.Form):
    """
    用于对博客发表评论
    """
    name = forms.CharField(label='称呼', max_length=16, error_messages = {
        'required':'请填写您的称呼',
        'max_length': '称呼太长',
    })
    email = forms.CharField(label='邮箱', error_messages={
        'required': '请填写您的邮箱',
        'max_length': '邮箱格式不正确',
    })
    content = forms.CharField(label='评论内容', error_messages = {
        'required': '请填写您的评论内容',
        'max_length': '评论内容太长',
    })