from typing import Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel # type: ignore
import openai  # type: ignore
from app.core.config import settings
from app.models.campaign import Campaign # type: ignore
from app.services.ai_service import AIService
from app.services.analytics_service import AnalyticsService # type: ignore

class MarketingService:
    def __init__(self):
        self.ai_service = AIService()
        self.analytics_service = AnalyticsService()
        self.openai = openai
        self.openai.api_key = settings.OPENAI_API_KEY
        
    async def create_campaign(self, data: Dict) -> Campaign:
        """Create a new marketing campaign"""
        try:
            # Generate content using AI
            content = await self.ai_service.generate_content(
                template=data["template"],
                target_audience=data["audience"],
                campaign_type=data["type"]
            )
            
            # Create campaign
            campaign = Campaign(
                name=data["name"],
                content=content,
                audience=data["audience"],
                type=data["type"],
                schedule=data["schedule"],
                status="draft"
            )
            
            return campaign
            
        except Exception as e:
            raise Exception(f"Campaign creation failed: {str(e)}")

    async def analyze_performance(self, campaign_id: int) -> Dict:
        """Analyze campaign performance"""
        try:
            return await self.analytics_service.get_campaign_metrics(campaign_id)
        except Exception as e:
            raise Exception(f"Analysis failed: {str(e)}") 

    async def generate_content(self, prompt: str, max_tokens: int = 500) -> str:
        """Generate content using OpenAI's GPT model"""
        try:
            response = await self.openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error generating content: {str(e)}")

    async def analyze_sentiment(self, text: str) -> Dict:
        """Analyze sentiment of content"""
        try:
            prompt = f"Analyze the sentiment of this text and return JSON with scores for positive, negative, and neutral: {text}"
            response = await self.generate_content(prompt)
            return eval(response)  # Convert string response to dict
        except Exception as e:
            raise Exception(f"Error analyzing sentiment: {str(e)}")

    async def optimize_seo(self, content: str, keywords: List[str]) -> str:
        """Optimize content for SEO"""
        try:
            prompt = f"Optimize this content for SEO using these keywords {keywords}: {content}"
            return await self.generate_content(prompt)
        except Exception as e:
            raise Exception(f"Error optimizing SEO: {str(e)}") 