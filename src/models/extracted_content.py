from pydantic import BaseModel
from typing import List

class ExtractedContent(BaseModel):
    main_content: List[str]
    datetime: List[str]
    prizemoney: List[str]