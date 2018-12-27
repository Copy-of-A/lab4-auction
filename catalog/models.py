from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import datetime


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
    name = models.CharField(max_length=200, help_text="Enter an auction name")
    start_time = models.DateTimeField(help_text="Enter a starting time")
    duration = models.DurationField(help_text="Enter a duration time")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,
                                 help_text="Select a category for this auction")

    @property
    def finish_time(self):
        return self.start_time + self.duration

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
    name = models.CharField(max_length=200, help_text="Enter a lot name")
    start_price = models.DecimalField(max_digits=10, decimal_places=1, blank=False, null=False,
                                      help_text="Enter a starting price")
    start_time = models.DateTimeField(help_text="Enter a starting time")
    duration = models.DurationField(help_text="Enter a duration time eg 3d 2:20:10")
    step = models.DecimalField(max_digits=5, decimal_places=1, blank=False, null=False,
                               help_text="Enter a starting price")
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # Foreign Key used because lot can only have one auction, but auctions can have multiple lots
    auction = models.ForeignKey(Auction, on_delete=models.SET_NULL, null=True)
    is_on_auction = models.BooleanField()
    is_sold = models.BooleanField()

    @property
    def finish_time(self):
        return self.start_time + self.duration

    @property
    def is_valid_for_buying(self):
        if not self.is_sold and datetime.datetime.now() > self.finish_time:
            return True
        return False

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


class User(AbstractUser):
    account = models.DecimalField(max_digits=10, decimal_places=1, blank=False, null=False)
    favourites = models.ManyToManyField(Category, on_delete=models.SET_NULL, null=True)
