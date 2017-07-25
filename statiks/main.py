import sys
from antlr4 import *
from TournamentSummaryLexer import TournamentSummaryLexer
from TournamentSummaryParser import TournamentSummaryParser
from TSParser import TSParser

def main(argv):
    input = FileStream(argv[1])
    lexer = TournamentSummaryLexer(input)
    stream = CommonTokenStream(lexer)
    parser = TournamentSummaryParser(stream)
    tree = parser.ts()
    printer = TSParser()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main(sys.argv)
