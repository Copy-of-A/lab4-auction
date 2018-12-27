from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Model representing a category of auction (e.g. Charity, Electronics etc.).
    """

    name = models.CharField(max_length=200, help_text="Enter a category of auction (e.g. Charity, Electronics etc.)")

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ["name"]

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Auction(models.Model):
    # пускай будет имя - почему бы и нет
    name = models.CharField(max_length=200, help_text="Enter an auction name")
    # время начала
    start_time = models.DateTimeField(help_text="Enter a starting time")
    # продолжительность аукциона
    duration = models.DurationField(help_text="Enter a duration time")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, help_text="Select a category for this auction")
    # ManyToManyField used because category can contain many auctions. Auctions can cover many categories.

    class Meta:
        ordering = ["name", "start_time"]

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('auction-detail', args=[str(self.id)])


class Lot(models.Model):
    # наименование лота
    name = models.CharField(max_length=200, help_text="Enter a lot name")
    # начальная цена
    start_price = models.DecimalField(max_digits=10, decimal_places=3, blank=False, null=False,
                                      help_text="Enter a starting price")
    # время начала
    start_time = models.DateTimeField(help_text="Enter a starting time")
    # продолжительность торгов
    duration = models.DurationField(help_text="Enter a duration time")
    # шаг ставки
    step = models.DecimalField(max_digits=10, decimal_places=3, blank=False, null=False,
                               help_text="Enter a starting price")
    # продавец
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # Foreign Key used because lot can only have one auction, but auctions can have multiple lots
    auction = models.ForeignKey(Auction, on_delete=models.SET_NULL, null=True)
    is_tender = models.BooleanField()
    is_sold = models.BooleanField()

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('lot-detail', args=[str(self.id)])
