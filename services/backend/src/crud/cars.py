import math
from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Cars
from src.schemas.cars import CarListSchema, CarOutSchema, PageResponse
from src.schemas.token import Status


async def get_cars():
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return await CarListSchema.from_queryset(Cars.all().limit(10))


async def get_car(car_id) -> CarOutSchema:
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return await CarOutSchema.from_queryset_single(Cars.get(id=car_id))


async def all_filter(payload):
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    offset = payload.limit * payload.page
    query = Cars.all()

    # total record
    total_record = await query.count() or 0
    # total page
    total_page = math.ceil(total_record / payload.limit)

    query = query.limit(payload.limit).offset(offset).order_by('-id')
    car_list = await CarListSchema.from_queryset(query)
    return PageResponse(
        content=car_list,
        page_number=payload.page,
        page_size=payload.limit,
        total_pages=total_page,
        total_record=total_record,
    )
