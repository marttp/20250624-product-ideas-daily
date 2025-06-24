from pydantic import BaseModel, Field
from typing import List
from enum import Enum


class BusinessDomain(str, Enum):
    """Business domain categories for product opportunities."""
    FINTECH = "fintech"
    HEALTHTECH = "healthtech"
    EDTECH = "edtech"
    SAAS = "saas"
    MARKETPLACE = "marketplace"
    ECOMMERCE = "ecommerce"
    PRODUCTIVITY = "productivity"
    SOCIAL = "social"
    GAMING = "gaming"
    ENTERPRISE = "enterprise"
    CONSUMER = "consumer"
    DEVTOOLS = "devtools"


class TargetMarket(str, Enum):
    """Target market categories."""
    B2B = "B2B"
    B2C = "B2C"
    B2B2C = "B2B2C"


class TechnicalFeasibility(str, Enum):
    """Technical complexity levels."""
    SIMPLE = "Simple"
    MEDIUM = "Medium"
    COMPLEX = "Complex"


class ProductOpportunity(BaseModel):
    """A single product opportunity with comprehensive analysis."""
    
    name: str = Field(
        description="Product name or title",
        min_length=1,
        max_length=100
    )
    
    concept: str = Field(
        description="Brief description of the product idea and what problem it solves",
        min_length=10,
        max_length=500
    )
    
    business_domain: BusinessDomain = Field(
        description="Business domain category (e.g., fintech, healthtech, saas)"
    )
    
    target_market: str = Field(
        description="Target market with specific segment details (e.g., 'B2B small businesses', 'B2C millennials')",
        min_length=5,
        max_length=200
    )
    
    unique_value_proposition: str = Field(
        description="What makes this solution unique and compelling compared to existing alternatives",
        min_length=10,
        max_length=300
    )
    
    technical_feasibility: TechnicalFeasibility = Field(
        description="Technical complexity assessment with key requirements"
    )
    
    internal_modules: List[str] = Field(
        description="List of key technical modules/components needed for implementation",
        min_items=3,
        max_items=10
    )
    
    implementation_cost: str = Field(
        description="Estimated monthly operational costs and initial development investment",
        min_length=10,
        max_length=300
    )
    
    risk_for_solopreneur: str = Field(
        description="Main risks and challenges for a solo developer/entrepreneur",
        min_length=10,
        max_length=300
    )
    
    source_url: str = Field(
        description="Reddit post or discussion URL that validated this need",
        min_length=10
    )


class ProductOpportunityReport(BaseModel):
    """Report containing top 5 product opportunities for solopreneurs."""
    
    opportunities: List[ProductOpportunity] = Field(
        description="List of exactly 5 product opportunities ranked by potential benefit",
        min_items=5,
        max_items=5
    )
    
    class Config:
        """Pydantic configuration."""
        json_encoders = {
            # Custom encoders if needed
        }
        schema_extra = {
            "example": {
                "opportunities": [
                    {
                        "name": "AI Resume Builder",
                        "concept": "An AI-powered resume builder that analyzes job descriptions and optimizes resumes for ATS systems while providing real-time feedback on content quality.",
                        "business_domain": "saas",
                        "target_market": "B2C job seekers and career changers",
                        "unique_value_proposition": "First resume builder with real-time ATS optimization and AI-powered content suggestions based on actual job posting analysis.",
                        "technical_feasibility": "Medium",
                        "internal_modules": [
                            "user_authentication_system",
                            "ai_content_analysis_engine",
                            "ats_optimization_algorithm",
                            "pdf_generation_service",
                            "payment_processing_module",
                            "job_posting_scraper"
                        ],
                        "implementation_cost": "Monthly: $150-300 (AI APIs, hosting). Initial development: 3-4 months solo work.",
                        "risk_for_solopreneur": "High competition from established players like Zety. Requires significant AI/ML expertise. Customer acquisition cost may be high.",
                        "source_url": "https://reddit.com/r/jobs/example"
                    }
                ]
            }
        }