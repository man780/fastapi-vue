from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Ads
from src.schemas.ads import AdOutSchema
from src.schemas.token import Status


async def get_ads():
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return await AdOutSchema.from_queryset(Ads.all().limit(10))


async def get_ad(ad_id) -> AdOutSchema:
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return await AdOutSchema.from_queryset_single(Ads.get(id=ad_id))


async def create_ad(ad, current_user) -> AdOutSchema:
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    ad_dict = ad.dict(exclude_unset=True)
    ad_dict["author_id"] = current_user.id
    ad_obj = await Ads.create(**ad_dict)
    return await AdOutSchema.from_tortoise_orm(ad_obj)


async def update_ad(ad_id, ad, current_user) -> AdOutSchema:
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    try:
        db_ad = await AdOutSchema.from_queryset_single(Ads.get(id=ad_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Ad {ad_id} not found")

    if db_ad.author.id == current_user.id:
        await Ads.filter(id=ad_id).update(**ad.dict(exclude_unset=True))
        return await AdOutSchema.from_queryset_single(Ads.get(id=ad_id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update")


async def delete_ad(ad_id, current_user) -> Status:
    """sumary_line
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    try:
        db_ad = await AdOutSchema.from_queryset_single(Ads.get(id=ad_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Ad {ad_id} not found")

    if db_ad.author.id == current_user.id:
        deleted_count = await Ads.filter(id=ad_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Ad {ad_id} not found")
        return Status(message=f"Deleted ad {ad_id}")

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")
