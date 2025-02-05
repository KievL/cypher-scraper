from .ai_chat import AIChat
from .information_extractor import InformationExtractor
from .raw_text_extractor import RawTextExtractor

from models.completion import Completion

from typing import List

class Interpreter:
    """
    Retrieve AI completions for the content of a list of websites.
    """

    def __init__(self, websites: List[str] = None):
        self.websites = websites

    def run(self, websites: List[str] = None) -> List[Completion]:
        """
        Runs the interpreter pipeline.
        """
        print("Interpreter running")