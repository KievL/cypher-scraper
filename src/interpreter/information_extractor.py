from typing import List

class InformationExtractor:
    """
    Information extractor for a given text (string). Extracts potential prizemoney, datetime and main info.
    """

    def __init__(self):
        pass

    def extract_main_info(self, text: str) -> List[str]:
        """
        Extracts the main info of a text. Returns a list of strings
        that are parts of the text potentially containing the main info.
        """
        pass

    def extract_datetime(self, text: str) -> List[str]:
        """
        Extracts parts of the text containg datetime text. Returns a list that contains the results.
        """
        pass

    def extract_prizemoney(self, text: str) -> List[str]:
        """
        Extracts parts of the text that potentially indicates prizemoneys. Returns a list that contains the results.
        """
        pass