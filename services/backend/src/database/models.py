from datetime import datetime
from tortoise import fields, models


class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    full_name = fields.CharField(max_length=50, null=True)
    password = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


class Notes(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=225)
    content = fields.TextField()
    author = fields.ForeignKeyField("models.Users", related_name="note")
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}, {self.author_id} on {self.created_at}"


class Ads(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=225)
    content = fields.TextField()
    ad_id = fields.UUIDField()
    advert_id = fields.UUIDField()
    url = fields.CharField(max_length=225, nullable=False)
    price = fields.IntField(nullable=False, default=0)
    make = fields.CharField(max_length=225, nullable=False, default="")
    model = fields.CharField(max_length=225, nullable=False, default="")
    color = fields.CharField(max_length=225, nullable=False, default="")
    year = fields.IntField(nullable=False, default=0)
    city = fields.CharField(max_length=225, nullable=False, default="")
    post_code = fields.CharField(max_length=225, nullable=False, default="")
    mileage = fields.IntField(nullable=False, default=0)
    doors = fields.IntField(nullable=False, default=0)
    fuel = fields.CharField(max_length=225, nullable=False, default="")
    transmission = fields.CharField(max_length=225, nullable=False, default="")
    body_style = fields.CharField(max_length=225, nullable=False, default="")
    engine_size = fields.IntField(nullable=False, default=0)
    seats = fields.IntField(nullable=False, default=0)
    hero_image = fields.CharField(max_length=225, nullable=False, default="")
    date = fields.DateField(default=datetime.now())
    car_type = fields.CharField(max_length=225, nullable=False, default="")
    dealer_domain = fields.CharField(max_length=225, nullable=False, default="")
    dealer_name = fields.CharField(max_length=225, nullable=False, default="")
    priority = fields.IntField(nullable=False, default=0)
    seller_type = fields.CharField(max_length=225, nullable=False, default="")
    vrm = fields.CharField(max_length=225, nullable=False, default="")

    created = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} on {self.created_at}"


class AdPictures(models.Model):
    id = fields.BigIntField(pk=True)
    url: str = fields.CharField(max_length=225, nullable=False)
    active: bool = fields.BooleanField(max_length=225, nullable=True, default=True)
    ad = fields.ForeignKeyField("models.Ads", related_name="ads")
    
    def __str__(self):
        return f"{self.url}, {self.ad_id} on {self.created_at}"
