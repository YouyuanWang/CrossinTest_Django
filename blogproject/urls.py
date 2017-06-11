
from django.conf.urls import url, include
from django.contrib import admin

from blog.feeds import AllPostsRssFeed

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'', include('comments.urls')),
    url(r'^all/rss/$', AllPostsRssFeed(), name='rss'),
]
