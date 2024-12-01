from fastapi import FastAPI # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from app.core.config import settings
from app.api.routes import router
from app.core.database import init_db
from app.services.marketing import (
    social_media_router,
    content_generation_router,
    email_marketing_router,
    seo_router,
    analytics_router,
    ads_router
)

app = FastAPI(
    title="Marketing AI Platform",
    description="Comprehensive AI-powered marketing services platform",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await init_db()

# Include all marketing service routers
app.include_router(router, prefix="/api")
app.include_router(social_media_router, prefix="/api/social-media", tags=["Social Media"])
app.include_router(content_generation_router, prefix="/api/content", tags=["Content Generation"])
app.include_router(email_marketing_router, prefix="/api/email", tags=["Email Marketing"])
app.include_router(seo_router, prefix="/api/seo", tags=["SEO"])
app.include_router(analytics_router, prefix="/api/analytics", tags=["Analytics"])
app.include_router(ads_router, prefix="/api/ads", tags=["Advertising"]) 