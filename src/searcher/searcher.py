from typing import List

class Searcher:
    """
    Uses GoogleSearch API to find target websites.
    """

    def __init__(self):
        pass

    def run(self, websites_quantity: int) -> List[str]:
        """
        Returns a list containing the desired websites URL.
        """
        print("Searcher running")