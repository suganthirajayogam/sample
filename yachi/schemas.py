"""
These schemas are the contract with the Flutter app. They map 1:1 onto
ChatMessage / SourceCitation / ProductSession in lib/models/chat_models.dart.
Keep field names in sync with that file when changing either side.
"""
from enum import Enum
from typing import Optional
from pydantic import BaseModel


class SourceType(str, Enum):
    excel_row = "excelRow"
    pdf_page = "pdfPage"
    image = "image"
    sql = "sql"


class SourceCitation(BaseModel):
    type: SourceType
    file_name: str
    detail: Optional[str] = None
    image_path: Optional[str] = None
    snippet: Optional[str] = None


class ConnectRequest(BaseModel):
    folder_path: str


class ConnectResponse(BaseModel):
    product_name: str
    file_count: int
    folder_path: str


class AskRequest(BaseModel):
    question: str
    folder_path: str


class AskResponse(BaseModel):
    text: str
    sources: list[SourceCitation] = []
    image_paths: list[str] = []
