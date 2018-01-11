# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/1/10
describle:
"""
from django.shortcuts import render_to_response
import datetime
from django.template import Context
from django.template.loader import get_template
def current_datetime(request):
    # now = datetime.datetime.now()
    # html = "<html><body>当前时间是 %s</body></html>"% now
    # return HttpResponse(html)

    # now = datetime.datetime.now()
    # t = Template("<html><body>当前时间是 {{ current_date}}</body></html>")
    # html = t.render(Context({'current_date': now}))
    # return HttpResponse(html)
    now = datetime.datetime.now()
    # fp = open('../mysite/templates/hello.html')
    # t = get_template('hello.html')
    # fp.close()
    # html = t.render(Context({'current_date': now}))
    return render_to_response('hello.html', {'current_date': now})

