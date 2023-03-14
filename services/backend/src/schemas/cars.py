from typing import Optional, List, TypeVar, Generic

from pydantic import BaseModel
from pydantic.generics import GenericModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Cars

T = TypeVar('T')

CarInSchema = pydantic_model_creator(Cars, name="CarIn", exclude = [
      "car_pictures", 
    ])
CarOutSchema = pydantic_model_creator(
    Cars, name="Car"
)

CarListSchema = pydantic_model_creator(Cars, name="CarList", include = [
    "id",
    "title",
    "ad_id",
    "url",
    "price",
    "make",
    "model",
    "color",
    "year",
    "city",
    "mileage",
    "hero_image",
    "seats",
    "doors",
    "color",
    "engine_size",
    "body_type",
    "fuel_type",
    "transmission"
])


class CarsFilter(GenericModel, Generic[T]):
    """Filtering"""
    page: int = 1
    limit: int = 10
    price: int
    year: int
    mileage: int
    gearbox: int
    engine_size: int
    colour: int
    fuel_type: int
    body_type: int
    doors: int
    seats: int
    make: str | None = None
    model: str | None = None


class PageResponse(GenericModel, Generic[T]):
    """ The response for a pagination query. """

    page_number: int
    page_size: int
    total_pages: int
    total_record: int
    content: List[CarListSchema]
