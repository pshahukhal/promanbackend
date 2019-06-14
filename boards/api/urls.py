from django.urls  import path
from django.conf.urls import url

from .views import BoardListView,BoardCreateView,BoardUpdateView,BoardDeleteView,BoardDetailView, ListListView,ListDetailView,ListCreateView,ListUpdateView,ListDeleteView,CardListView,CardDetailView,CardCreateView,CardUpdateView,CardDeleteView

urlpatterns = [
    url('^boards$',BoardListView.as_view()),
    url('^boards/(?P<pk>\d+)$',BoardDetailView.as_view()),
    url('^boards/create',BoardCreateView.as_view()),
    url('^boards/update/(?P<pk>\d+)$',BoardUpdateView.as_view()),
    url('^boards/delete/(?P<pk>\d+)$',BoardDeleteView.as_view()),
    url('^lists$',ListListView.as_view()),
    url('^lists/(?P<pk>\d+)$',ListDetailView.as_view()),
    url('^lists/create',ListCreateView.as_view()),
    url('^lists/update/(?P<pk>\d+)$',ListUpdateView.as_view()),
    url('^lists/delete/(?P<pk>\d+)$',ListDeleteView.as_view()),
    url('^cards$',CardListView.as_view()),
    url('^cards/(?P<pk>\d+)$',CardDetailView.as_view()),
    url('^cards/create',CardCreateView.as_view()),
    url('^cards/update/(?P<pk>\d+)$',CardUpdateView.as_view()),
    url('^cards/delete/(?P<pk>\d+)$',CardDeleteView.as_view()),
]