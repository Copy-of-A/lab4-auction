from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lots/$', views.LotListView.as_view(), name='lots'),
    url(r'^lot/(?P<pk>\d+)$', views.LotDetailView.as_view(), name='lot-detail'),
    url(r'^auctions/$', views.AuctionListView.as_view(), name='auctions'),
    url(r'^auction/(?P<pk>\d+)$', views.AuctionDetailView.as_view(), name='auction-detail'),
    url(r'^mylots/$', views.LotsForSaleByUserListView.as_view(), name='my-for-sale'),
]
