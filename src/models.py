# Import Dependencies
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class CompanyAnalysis(BaseModel):
    """Structured output for LLM company analysis focused on developer tools"""
    pricing_model: str # Free, Freemium, Paid, Enterprise, Unknown
    is_open_source: Optional[bool] = None
    tech_stack: List[str] = Field(default_factory=list)
    description: str = ""
    api_available: Optional[bool] = None
    language_support: List[str] = Field(default_factory=list)
    integration_capabilities: List[str] = Field(default_factory=list)


class CompanyInfo(BaseModel):
    """Basic information about a company"""
    name: str
    description: str
    website: Optional[str] = None
    industry: Optional[str] = None
    pricing_model: Optional[str] = None
    is_open_source: Optional[bool] = None
    tech_stack: List[str] = Field(default_factory=list)
    competitors: List[str] = Field(default_factory=list)
    # Developer-specific fields
    api_available: Optional[bool] = None
    language_support: List[str] = Field(default_factory=list)
    integration_capabilities: List[str] = Field(default_factory=list)
    developer_experience_rating: Optional[str] = None # e.g., Excellent, Good, Fair, Poor


class ResearchState(BaseModel):
    query: str
    extracted_tools: List[str] = Field(default_factory=list)
    companies: List[CompanyInfo] = Field(default_factory=list)
    search_results: List[Dict[str, Any]] = Field(default_factory=list)
    analysis: Optional[str] = None
