import sys
from antlr4 import *
from statiks.TS import TS
from statiks.grammars.TSParserLexer import TSParserLexer
from statiks.grammars.TSParserParser import TSParserParser


def main(argv):
    input = FileStream(argv[1])
    lexer = TSParserLexer(input)
    stream = CommonTokenStream(lexer)
    parser = TSParserParser(stream)
    tree = parser.ts()
    printer =  TS()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

main(sys.argv)
