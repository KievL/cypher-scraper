from pydantic import BaseModel

class Completion(BaseModel):
    main_content: str
    datetime: str
    prizemoney: str