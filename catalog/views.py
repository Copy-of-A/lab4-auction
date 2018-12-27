# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Auction, Lot
from django.views import generic

# Create your views here.


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_auctions = Auction.objects.all().count()
    num_lots = Lot.objects.all().count()
    # Непроданные лоты
    # num_lots_available = Lot.objects.filter(is_sold='True').count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_auctions': num_auctions, 'num_lots': num_lots, 'num_visits': num_visits},
    )


class LotListView(generic.ListView):
    model = Lot
    paginate_by = 10


class LotDetailView(generic.DetailView):
    model = Lot


class AuctionListView(generic.ListView):
    model = Auction
    paginate_by = 10


class AuctionDetailView(generic.DetailView):
    model = Auction

