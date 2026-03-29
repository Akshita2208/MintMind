from pydantic import BaseModel
from datetime import datetime
from typing import Any, Dict

class ReportResponse(BaseModel):
    id: str
    user_id: str
    file_name: str
    report_type: str
    result: Dict[str, Any]
    created_at: datetime
