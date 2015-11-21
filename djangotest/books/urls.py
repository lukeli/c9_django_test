from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^addauthor$', views.manage_author, name='author'),
    #url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    #url(r'^(?P<author_id>[0-9]+)/add/$', views.manage_books, name='add_book'),
    
    
]