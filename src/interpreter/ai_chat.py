import os

from models.extracted_content import ExtractedContent
from models.completion import Completion

class AIChat:
    """
    API from OpenAI that is built to output a completion about the gathered text.
    """

    def __init__(self, content : ExtractedContent = None):
        self.api_key = os.getenv("OPENAI_API_KEY") # ask for the api key in the whatsapp group
        self.content = content

    def get_completion(self, content : ExtractedContent = None) -> Completion:
        """
        Get the completion from the OpenAPI for the extracted content.
        """
        self.content = content if content is not None else self.content