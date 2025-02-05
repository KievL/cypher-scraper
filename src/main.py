from searcher.searcher import Searcher
from interpreter.interpreter import Interpreter
from dotenv import load_dotenv

# run searcher and interpreter

class Cypher:
    def __init__(self):
        pass

    def run(self):
        searcher = Searcher()
        interpreter = Interpreter()

        searcher.run()
        interpreter.run()

if __name__=="__main__":
    load_dotenv()

    cypher = Cypher()

    cypher.run()