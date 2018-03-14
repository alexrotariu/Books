from django.conf.urls import url
from books.views import *
from . import views

urlpatterns = [
    url(r'^$', BookList.as_view(), name='books'),
    url(r'^author/(?P<author_slug>[a-z0-9-]+)/$', views.book_list_by_author, name='books-author'),
    url(r'^(?P<pk>[0-9]+)/$', BookDetail.as_view(), name='book'),
    url(r'^add/$', BookAdd.as_view(), name='book-add'),
    url(r'^add/thanks$', BookAddThanks.as_view(), name='add-thanks'),
    url(r'^(?P<pk>[0-9]+)/delete/$', BookDelete.as_view(), name='book-delete'),
    url(r'^(?P<pk>[0-9]+)/edit/$', BookEdit.as_view(), name='book-edit'),
    url(r'^about/$', views.about, name='about'),
]