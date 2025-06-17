from typing import List, Optional, Dict, Any, Union
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, HttpUrl


class HTTPMethod(str, Enum):
    """HTTP methods for API endpoints."""
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


class ParameterType(str, Enum):
    """Parameter types for API endpoints."""
    STRING = "string"
    INTEGER = "integer"
    BOOLEAN = "boolean"
    ARRAY = "array"
    OBJECT = "object"
    NUMBER = "number"


class ParameterLocation(str, Enum):
    """Where the parameter is located in the request."""
    QUERY = "query"
    PATH = "path"
    HEADER = "header"
    BODY = "body"
    FORM = "form"


class Parameter(BaseModel):
    """Represents an API parameter."""
    name: str
    type: ParameterType
    location: ParameterLocation
    required: bool = False
    description: Optional[str] = None
    default_value: Optional[Union[str, int, bool, float]] = None
    example: Optional[str] = None
    enum_values: Optional[List[str]] = None
    min_value: Optional[Union[int, float]] = None
    max_value: Optional[Union[int, float]] = None
    pattern: Optional[str] = None


class Response(BaseModel):
    """Represents an API response."""
    status_code: int
    description: Optional[str] = None
    content_type: str = "application/json"
    response_schema: Optional[Dict[str, Any]] = None
    example: Optional[Dict[str, Any]] = None


class ErrorCode(BaseModel):
    """Represents an API error code."""
    code: Union[str, int]
    message: str
    description: Optional[str] = None
    http_status: Optional[int] = None


class Example(BaseModel):
    """Represents a request/response example."""
    title: str
    description: Optional[str] = None
    request: Optional[Dict[str, Any]] = None
    response: Optional[Dict[str, Any]] = None


class APIEndpoint(BaseModel):
    """Represents a single API endpoint."""
    name: str
    method: HTTPMethod
    path: str
    description: Optional[str] = None
    summary: Optional[str] = None
    parameters: List[Parameter] = Field(default_factory=list)
    responses: List[Response] = Field(default_factory=list)
    error_codes: List[ErrorCode] = Field(default_factory=list)
    examples: List[Example] = Field(default_factory=list)
    tags: List[str] = Field(default_factory=list)
    deprecated: bool = False
    rate_limit: Optional[str] = None
    authentication_required: bool = True
    scope: Optional[List[str]] = None


class APIDocumentation(BaseModel):
    """Represents complete API documentation for a platform."""
    platform: str  # e.g., "shopee", "tiktok", "lazada"
    title: str
    version: str
    description: Optional[str] = None
    base_url: Optional[HttpUrl] = None
    endpoints: List[APIEndpoint] = Field(default_factory=list)
    scraped_at: datetime = Field(default_factory=datetime.now)
    source_url: Optional[HttpUrl] = None
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        } 