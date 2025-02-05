
class RawTextExtractor:
    """
    Extracts texts from HTML websites and PDFs.
    """

    def __init__(self, website: str = None):
        self.website = website

    def extract(self, website: str = None) -> str:
        """
        Extracts the text from the given website. Returns a string with the entire website content (html and PDFs...).
        """
        self.website = website if website is not None else self.website

