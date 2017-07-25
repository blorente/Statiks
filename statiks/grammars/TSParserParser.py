# Generated from TSParser.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\33")
        buf.write("T\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\5\t>\n\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\5\nH\n\n\3\n\5\nK\n\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\2\2")
        buf.write("L\2\26\3\2\2\2\4\36\3\2\2\2\6$\3\2\2\2\b(\3\2\2\2\n.\3")
        buf.write("\2\2\2\f\61\3\2\2\2\16\67\3\2\2\2\20=\3\2\2\2\22?\3\2")
        buf.write("\2\2\24N\3\2\2\2\26\27\5\4\3\2\27\30\5\6\4\2\30\31\5\n")
        buf.write("\6\2\31\32\5\f\7\2\32\33\7\30\2\2\33\34\5\16\b\2\34\35")
        buf.write("\7\27\2\2\35\3\3\2\2\2\36\37\7\3\2\2\37 \7\24\2\2 !\7")
        buf.write("\4\2\2!\"\7\23\2\2\"#\7\31\2\2#\5\3\2\2\2$%\7\5\2\2%&")
        buf.write("\5\b\5\2&\'\7\31\2\2\'\7\3\2\2\2()\7\22\2\2)*\7\6\2\2")
        buf.write("*+\7\22\2\2+,\7\7\2\2,-\7\20\2\2-\t\3\2\2\2./\7\21\2\2")
        buf.write("/\60\7\31\2\2\60\13\3\2\2\2\61\62\7\b\2\2\62\63\7\22\2")
        buf.write("\2\63\64\7\7\2\2\64\65\7\20\2\2\65\66\7\31\2\2\66\r\3")
        buf.write("\2\2\2\678\5\20\t\28\17\3\2\2\29:\5\22\n\2:;\5\20\t\2")
        buf.write(";>\3\2\2\2<>\5\22\n\2=9\3\2\2\2=<\3\2\2\2>\21\3\2\2\2")
        buf.write("?@\7\t\2\2@A\7\33\2\2AB\7\n\2\2BC\7\33\2\2CD\7\13\2\2")
        buf.write("DE\7\33\2\2EJ\7\f\2\2FH\5\24\13\2GF\3\2\2\2GH\3\2\2\2")
        buf.write("HK\3\2\2\2IK\7\r\2\2JG\3\2\2\2JI\3\2\2\2KL\3\2\2\2LM\7")
        buf.write("\31\2\2M\23\3\2\2\2NO\7\22\2\2OP\7\16\2\2PQ\7\25\2\2Q")
        buf.write("R\7\17\2\2R\25\3\2\2\2\5=GJ")
        return buf.getvalue()


class TSParserParser ( Parser ):

    grammarFileName = "TSParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'PokerStars Tournament '", "', '", "'Buy-In: '", 
                     "'/'", "' '", "'Total Prize Pool: '", "'  '", "': '", 
                     "' ('", "'),'", "' still playing'", "'('", "')'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'No Limit Hold'em'", "<INVALID>", 
                     "<INVALID>", "'Tournament started '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "CUR", "PLAYERS", "MONEY", 
                      "GAME", "TID", "PERCENTAGE", "TOURNSTARTED", "PERSONAL", 
                      "DATETIME", "NEWLINE", "PLACESUFFIX", "WORDS" ]

    RULE_ts = 0
    RULE_description = 1
    RULE_buyin = 2
    RULE_buyincost = 3
    RULE_players = 4
    RULE_prizepool = 5
    RULE_results = 6
    RULE_playerlist = 7
    RULE_player = 8
    RULE_prize = 9

    ruleNames =  [ "ts", "description", "buyin", "buyincost", "players", 
                   "prizepool", "results", "playerlist", "player", "prize" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    CUR=14
    PLAYERS=15
    MONEY=16
    GAME=17
    TID=18
    PERCENTAGE=19
    TOURNSTARTED=20
    PERSONAL=21
    DATETIME=22
    NEWLINE=23
    PLACESUFFIX=24
    WORDS=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class TsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def description(self):
            return self.getTypedRuleContext(TSParserParser.DescriptionContext,0)


        def buyin(self):
            return self.getTypedRuleContext(TSParserParser.BuyinContext,0)


        def players(self):
            return self.getTypedRuleContext(TSParserParser.PlayersContext,0)


        def prizepool(self):
            return self.getTypedRuleContext(TSParserParser.PrizepoolContext,0)


        def DATETIME(self):
            return self.getToken(TSParserParser.DATETIME, 0)

        def results(self):
            return self.getTypedRuleContext(TSParserParser.ResultsContext,0)


        def PERSONAL(self):
            return self.getToken(TSParserParser.PERSONAL, 0)

        def getRuleIndex(self):
            return TSParserParser.RULE_ts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTs" ):
                listener.enterTs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTs" ):
                listener.exitTs(self)




    def ts(self):

        localctx = TSParserParser.TsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ts)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.description()
            self.state = 21
            self.buyin()
            self.state = 22
            self.players()
            self.state = 23
            self.prizepool()
            self.state = 24
            self.match(TSParserParser.DATETIME)
            self.state = 25
            self.results()
            self.state = 26
            self.match(TSParserParser.PERSONAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DescriptionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TID(self):
            return self.getToken(TSParserParser.TID, 0)

        def GAME(self):
            return self.getToken(TSParserParser.GAME, 0)

        def NEWLINE(self):
            return self.getToken(TSParserParser.NEWLINE, 0)

        def getRuleIndex(self):
            return TSParserParser.RULE_description

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDescription" ):
                listener.enterDescription(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDescription" ):
                listener.exitDescription(self)




    def description(self):

        localctx = TSParserParser.DescriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_description)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(TSParserParser.T__0)
            self.state = 29
            self.match(TSParserParser.TID)
            self.state = 30
            self.match(TSParserParser.T__1)
            self.state = 31
            self.match(TSParserParser.GAME)
            self.state = 32
            self.match(TSParserParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BuyinContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.cost = None # BuyincostContext

        def NEWLINE(self):
            return self.getToken(TSParserParser.NEWLINE, 0)

        def buyincost(self):
            return self.getTypedRuleContext(TSParserParser.BuyincostContext,0)


        def getRuleIndex(self):
            return TSParserParser.RULE_buyin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuyin" ):
                listener.enterBuyin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuyin" ):
                listener.exitBuyin(self)




    def buyin(self):

        localctx = TSParserParser.BuyinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_buyin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(TSParserParser.T__2)
            self.state = 35
            localctx.cost = self.buyincost()
            self.state = 36
            self.match(TSParserParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BuyincostContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MONEY(self, i:int=None):
            if i is None:
                return self.getTokens(TSParserParser.MONEY)
            else:
                return self.getToken(TSParserParser.MONEY, i)

        def CUR(self):
            return self.getToken(TSParserParser.CUR, 0)

        def getRuleIndex(self):
            return TSParserParser.RULE_buyincost

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuyincost" ):
                listener.enterBuyincost(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuyincost" ):
                listener.exitBuyincost(self)




    def buyincost(self):

        localctx = TSParserParser.BuyincostContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_buyincost)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(TSParserParser.MONEY)
            self.state = 39
            self.match(TSParserParser.T__3)
            self.state = 40
            self.match(TSParserParser.MONEY)
            self.state = 41
            self.match(TSParserParser.T__4)
            self.state = 42
            self.match(TSParserParser.CUR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PlayersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLAYERS(self):
            return self.getToken(TSParserParser.PLAYERS, 0)

        def NEWLINE(self):
            return self.getToken(TSParserParser.NEWLINE, 0)

        def getRuleIndex(self):
            return TSParserParser.RULE_players

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlayers" ):
                listener.enterPlayers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlayers" ):
                listener.exitPlayers(self)




    def players(self):

        localctx = TSParserParser.PlayersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_players)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(TSParserParser.PLAYERS)
            self.state = 45
            self.match(TSParserParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrizepoolContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MONEY(self):
            return self.getToken(TSParserParser.MONEY, 0)

        def CUR(self):
            return self.getToken(TSParserParser.CUR, 0)

        def NEWLINE(self):
            return self.getToken(TSParserParser.NEWLINE, 0)

        def getRuleIndex(self):
            return TSParserParser.RULE_prizepool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrizepool" ):
                listener.enterPrizepool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrizepool" ):
                listener.exitPrizepool(self)




    def prizepool(self):

        localctx = TSParserParser.PrizepoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_prizepool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(TSParserParser.T__5)
            self.state = 48
            self.match(TSParserParser.MONEY)
            self.state = 49
            self.match(TSParserParser.T__4)
            self.state = 50
            self.match(TSParserParser.CUR)
            self.state = 51
            self.match(TSParserParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ResultsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def playerlist(self):
            return self.getTypedRuleContext(TSParserParser.PlayerlistContext,0)


        def getRuleIndex(self):
            return TSParserParser.RULE_results

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResults" ):
                listener.enterResults(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResults" ):
                listener.exitResults(self)




    def results(self):

        localctx = TSParserParser.ResultsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_results)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.playerlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PlayerlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def player(self):
            return self.getTypedRuleContext(TSParserParser.PlayerContext,0)


        def playerlist(self):
            return self.getTypedRuleContext(TSParserParser.PlayerlistContext,0)


        def getRuleIndex(self):
            return TSParserParser.RULE_playerlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlayerlist" ):
                listener.enterPlayerlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlayerlist" ):
                listener.exitPlayerlist(self)




    def playerlist(self):

        localctx = TSParserParser.PlayerlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_playerlist)
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.player()
                self.state = 56
                self.playerlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.player()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PlayerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORDS(self, i:int=None):
            if i is None:
                return self.getTokens(TSParserParser.WORDS)
            else:
                return self.getToken(TSParserParser.WORDS, i)

        def NEWLINE(self):
            return self.getToken(TSParserParser.NEWLINE, 0)

        def prize(self):
            return self.getTypedRuleContext(TSParserParser.PrizeContext,0)


        def getRuleIndex(self):
            return TSParserParser.RULE_player

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlayer" ):
                listener.enterPlayer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlayer" ):
                listener.exitPlayer(self)




    def player(self):

        localctx = TSParserParser.PlayerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_player)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(TSParserParser.T__6)
            self.state = 62
            self.match(TSParserParser.WORDS)
            self.state = 63
            self.match(TSParserParser.T__7)
            self.state = 64
            self.match(TSParserParser.WORDS)
            self.state = 65
            self.match(TSParserParser.T__8)
            self.state = 66
            self.match(TSParserParser.WORDS)
            self.state = 67
            self.match(TSParserParser.T__9)
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TSParserParser.MONEY, TSParserParser.NEWLINE]:
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TSParserParser.MONEY:
                    self.state = 68
                    self.prize()


                pass
            elif token in [TSParserParser.T__10]:
                self.state = 71
                self.match(TSParserParser.T__10)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 74
            self.match(TSParserParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrizeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MONEY(self):
            return self.getToken(TSParserParser.MONEY, 0)

        def PERCENTAGE(self):
            return self.getToken(TSParserParser.PERCENTAGE, 0)

        def getRuleIndex(self):
            return TSParserParser.RULE_prize

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrize" ):
                listener.enterPrize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrize" ):
                listener.exitPrize(self)




    def prize(self):

        localctx = TSParserParser.PrizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_prize)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(TSParserParser.MONEY)
            self.state = 77
            self.match(TSParserParser.T__11)
            self.state = 78
            self.match(TSParserParser.PERCENTAGE)
            self.state = 79
            self.match(TSParserParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





