from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.ads as crud
from src.auth.jwthandler import get_current_user
from src.schemas.ads import AdOutSchema, AdInSchema, UpdateAd
from src.schemas.token import Status
from src.schemas.users import UserOutSchema


router = APIRouter(tags=["Ads"])


@router.get(
    "/ads",
    response_model=List[AdOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_ads():
    return await crud.get_ads()


@router.get(
    "/ad/{ad_id}",
    response_model=AdOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_ad(ad_id: int) -> AdOutSchema:
    try:
        return await crud.get_ad(ad_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Ad does not exist",
        )


@router.post(
    "/ads", response_model=AdOutSchema, dependencies=[Depends(get_current_user)]
)
async def create_ad(
    ad: AdInSchema, current_user: UserOutSchema = Depends(get_current_user)
) -> AdOutSchema:
    return await crud.create_ad(ad, current_user)


@router.patch(
    "/ad/{ad_id}",
    dependencies=[Depends(get_current_user)],
    response_model=AdOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_ad(
    ad_id: int,
    ad: UpdateAd,
    current_user: UserOutSchema = Depends(get_current_user),
) -> AdOutSchema:
    return await crud.update_ad(ad_id, ad, current_user)


@router.delete(
    "/ad/{ad_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_ad(
    ad_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_ad(ad_id, current_user)
