from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class ContactInfo(BaseModel):
    """Contact information model"""
    email: Optional[str] = Field(None, description="Email address")
    phone: Optional[str] = Field(None, description="Phone number")
    linkedin: Optional[str] = Field(None, description="LinkedIn profile URL")
    github: Optional[str] = Field(None, description="GitHub profile URL")
    website: Optional[str] = Field(None, description="Personal website URL")
    address: Optional[str] = Field(None, description="Address or location")

class Education(BaseModel):
    """Education entry model"""
    institution: str = Field(..., description="Name of the educational institution")
    degree: str = Field(..., description="Degree or qualification obtained")
    field_of_study: Optional[str] = Field(None, description="Field of study or major")
    start_date: Optional[str] = Field(None, description="Start date (YYYY-MM or YYYY)")
    end_date: Optional[str] = Field(None, description="End date (YYYY-MM or YYYY)")
    gpa: Optional[str] = Field(None, description="GPA or grade")
    location: Optional[str] = Field(None, description="Location of institution")

class Experience(BaseModel):
    """Work experience entry model"""
    company: str = Field(..., description="Company name")
    position: str = Field(..., description="Job title or position")
    start_date: Optional[str] = Field(None, description="Start date (YYYY-MM or YYYY)")
    end_date: Optional[str] = Field(None, description="End date (YYYY-MM or YYYY)")
    location: Optional[str] = Field(None, description="Location of work")
    description: Optional[str] = Field(None, description="Job description and responsibilities")
    achievements: Optional[List[str]] = Field(None, description="Key achievements or accomplishments")

class Project(BaseModel):
    """Project entry model"""
    name: str = Field(..., description="Project name")
    description: Optional[str] = Field(None, description="Project description")
    technologies: Optional[List[str]] = Field(None, description="Technologies used")
    start_date: Optional[str] = Field(None, description="Start date")
    end_date: Optional[str] = Field(None, description="End date")
    url: Optional[str] = Field(None, description="Project URL or repository")

class Certification(BaseModel):
    """Certification entry model"""
    name: Optional[str] = Field(..., description="Certification name")
    issuer: Optional[str] = Field(..., description="Issuing organization")
    date_obtained: Optional[str] = Field(None, description="Date obtained")
    expiry_date: Optional[str] = Field(None, description="Expiry date")
    credential_id: Optional[str] = Field(None, description="Credential ID")

class ParsedCV(BaseModel):
    """Main CV data model"""
    name: str = Field(..., description="Full name of the person")
    contact_info: ContactInfo = Field(..., description="Contact information")
    summary: Optional[str] = Field(None, description="Professional summary or objective")
    experience: List[Experience] = Field(default_factory=list, description="Work experience")
    education: List[Education] = Field(default_factory=list, description="Educational background")
    skills: List[str] = Field(default_factory=list, description="Technical and soft skills")
    projects: List[Project] = Field(default_factory=list, description="Projects")
    certifications: List[Certification] = Field(default_factory=list, description="Certifications")
    languages: List[str] = Field(default_factory=list, description="Languages spoken")
    awards: List[str] = Field(default_factory=list, description="Awards and honors")
    volunteer_experience: Optional[str] = Field(None, description="Volunteer experience")
    hobbies: Optional[str] = Field(None, description="Hobbies and interests")