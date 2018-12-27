from django.shortcuts import render
from .models import Auction, Lot, Category

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

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_auctions': num_auctions, 'num_lots': num_lots},
    )
