from fastapi import APIRouter, HTTPException # type: ignore
from typing import List, Dict
from app.services.marketing_service import MarketingService
from app.services.email_service import EmailService # type: ignore
from app.services.social_media_service import SocialMediaService # type: ignore

router = APIRouter()
marketing_service = MarketingService()
email_service = EmailService()
social_service = SocialMediaService()

@router.post("/campaigns/")
async def create_campaign(campaign_data: Dict):
    try:
        campaign = await marketing_service.create_campaign(campaign_data)
        return campaign
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/email/campaign/")
async def create_email_campaign(campaign_data: Dict):
    try:
        campaign = await email_service.create_email_campaign(campaign_data)
        return campaign
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/social/campaign/")
async def create_social_campaign(campaign_data: Dict):
    try:
        posts = await social_service.create_social_campaign(campaign_data)
        return posts
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/analytics/campaign/{campaign_id}")
async def get_campaign_analytics(campaign_id: int):
    try:
        analytics = await marketing_service.analyze_performance(campaign_id)
        return analytics
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 