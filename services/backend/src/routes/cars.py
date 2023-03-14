from typing import List

from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist

import src.crud.cars as crud
from src.schemas.cars import CarOutSchema, CarListSchema, CarsFilter
from src.schemas.token import Status


router = APIRouter(tags=["Cars"])


@router.get(
    "/cars",
    response_model=List[CarListSchema],
)
async def get_cars():
    return await crud.get_cars()


@router.post("/all/", status_code=status.HTTP_200_OK)
async def all_cars(
    payload: CarsFilter
):
    """Car list with filtering"""
    cars = await crud.all_filter(payload=payload)
    return cars


@router.get(
    "/car/{car_id}",
    response_model=CarOutSchema,
)
async def get_car(car_id: int) -> CarOutSchema:
    try:
        return await crud.get_car(car_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Car does not exist",
        )
