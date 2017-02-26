"""echo_ua_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
# from django.contrib import admin
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]

from django.conf.urls import include, url
from student.views import studentlist, edit_student
from group.views import grouplist, edit_group
from loginsys.views import delete_instance
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
urlpatterns = [
                       # Examples:
                       # url(r'^$', 'steelkiwi_test.views.home', name='home'),
                       # url(r'^steelkiwi_test/', include('steelkiwi_test.foo.urls')),
                       url(r'^$', grouplist, name='index'),
                       url(r'^group/(\d+)/$', studentlist, name='show_group'),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^login/$', auth_views.login,  TemplateView.as_view(template_name = 'login1.html'), name='login'),
                       url(r'^logout/$', auth_views.logout, {'login_url': '/login/'}, name='logout'),
                       # url(r'^accounts/profile/', 'django.views.generic.simple.redirect_to', {'url': '/'}),
                       url(r'^student/add/$', edit_student, name='add_student'),
                       url(r'^student/add/(?P<group_id>\d+)/$', edit_student, name='add_student_to_group'),
                       url(r'^student/edit/(\d+)/$', edit_student, name='edit_student'),

                       url(r'^group/add/$', edit_group, name='add_group'),
                       url(r'^group/edit/(\d+)/$', edit_group, name='edit_group'),

                       url(r'^student/delete/(?P<instance_id>\d+)/',
                           delete_instance,
                           name='delete_student',
                           kwargs={'instance_type': 1}),

                       url(r'^group/delete/(?P<instance_id>\d+)/',
                           delete_instance,
                           name='delete_group',
                           kwargs={'instance_type': 2}),
                       ]
