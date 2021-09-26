from django.db import models
from django.db.models.fields.files import ImageField
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


# Create your models here.
# room only have on host but room can have many room tyeps (manytomany)


class AbstractItem(core_models.TimeStampedModel):
    """abstract item 입니다"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    class Meta:
        ordering = ["created"]


class Amenities(AbstractItem):
    pass


class Facility(AbstractItem):
    pass


class HouseRules(AbstractItem):
    class Meta:
        verbose_name_plural = "House Rule"


class Room(core_models.TimeStampedModel):

    """room model definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    guests = models.IntegerField()
    address = models.CharField(max_length=180)
    bedrooms = models.IntegerField()
    bath = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenities, blank=True)
    facility = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(HouseRules, blank=True)

    def __str__(self):
        return self.name


class Photo(AbstractItem):
    caption = models.CharField(max_length=80)
    file = ImageField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
