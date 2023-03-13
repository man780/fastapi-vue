from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Ads


AdInSchema = pydantic_model_creator(Ads, name="AdIn", exclude_readonly=True)
AdOutSchema = pydantic_model_creator(
    Ads, name="Ad", exclude =[
      "created",
    ]
)


class UpdateAd(BaseModel):
    title: Optional[str]
    content: Optional[str]
