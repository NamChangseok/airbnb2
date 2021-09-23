from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import BooleanField

# Create your models here.


class User(AbstractUser):

    """ custom user model 입니다."""

    gender_male = "male"
    gender_female = "female"
    gender_other = "other"

    gender_choices = (
        (gender_male, "male"),
        (gender_female, "female"),
        (gender_other, "other"),
    )

    language_english = "english"
    language_korean = "korean"

    language_choice = (
        (language_korean, "korean"),
        (language_english, "english"),
    )
    currency_usd = "usd"
    currency_kr = "krw"

    currency_choice = (
        (currency_kr, "krwon"),
        (currency_usd, "usdollar"),
    )

    currency = models.CharField(
        choices=currency_choice, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default="")
    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=gender_choices, max_length=10, null=True)
    language = models.CharField(
        choices=language_choice, max_length=10, null=True, blank=True
    )

    superhost = BooleanField(default=False)
