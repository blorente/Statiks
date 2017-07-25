# Generated from ../TournamentSummary.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3!")
        buf.write("Y\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\5\nB\n\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\5\13K\n\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\2\2\16\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\2\2\2N\2\32\3\2\2\2\4#\3\2\2")
        buf.write("\2\6(\3\2\2\2\b-\3\2\2\2\n\61\3\2\2\2\f\64\3\2\2\2\16")
        buf.write("8\3\2\2\2\20;\3\2\2\2\22A\3\2\2\2\24C\3\2\2\2\26L\3\2")
        buf.write("\2\2\30Q\3\2\2\2\32\33\5\4\3\2\33\34\5\6\4\2\34\35\5\b")
        buf.write("\5\2\35\36\5\n\6\2\36\37\5\f\7\2\37 \5\16\b\2 !\5\20\t")
        buf.write("\2!\"\5\30\r\2\"\3\3\2\2\2#$\7\21\2\2$%\7\22\2\2%&\7\23")
        buf.write("\2\2&\'\7\24\2\2\'\5\3\2\2\2()\7\3\2\2)*\7\22\2\2*+\7")
        buf.write("\4\2\2+,\7\23\2\2,\7\3\2\2\2-.\7\5\2\2./\7\24\2\2/\60")
        buf.write("\7\27\2\2\60\t\3\2\2\2\61\62\7\30\2\2\62\63\7\6\2\2\63")
        buf.write("\13\3\2\2\2\64\65\7\7\2\2\65\66\7\25\2\2\66\67\7\27\2")
        buf.write("\2\67\r\3\2\2\289\7\b\2\29:\7\31\2\2:\17\3\2\2\2;<\5\22")
        buf.write("\n\2<\21\3\2\2\2=>\5\24\13\2>?\5\22\n\2?B\3\2\2\2@B\5")
        buf.write("\24\13\2A=\3\2\2\2A@\3\2\2\2B\23\3\2\2\2CD\7\32\2\2DE")
        buf.write("\7\t\2\2EF\7\33\2\2FG\7\n\2\2GH\7\34\2\2HJ\7\13\2\2IK")
        buf.write("\5\26\f\2JI\3\2\2\2JK\3\2\2\2K\25\3\2\2\2LM\7\25\2\2M")
        buf.write("N\7\n\2\2NO\7\35\2\2OP\7\f\2\2P\27\3\2\2\2QR\7\r\2\2R")
        buf.write("S\7\36\2\2ST\7\16\2\2TU\7\17\2\2UV\7\37\2\2VW\7\20\2\2")
        buf.write("W\31\3\2\2\2\4AJ")
        return buf.getvalue()


class TournamentSummaryParser ( Parser ):

    grammarFileName = "TournamentSummary.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'PokerStars Tournament '", "','", "'Buy-In:'", 
                     "'players'", "'Total Prize Pool:'", "'Tournament started'", 
                     "':'", "'('", "'),'", "')'", "'You finished in'", "'place'", 
                     "'(eliminated at hand'", "').'", "<INVALID>", "<INVALID>", 
                     "'No Limit Hold'em'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "TSNAME", "TID", 
                      "GAME", "BUYIN", "MONEY", "CURSIGN", "CUR", "PLAYERNUM", 
                      "DATE", "RESULT", "NICKNAME", "LOCATION", "PERCENTAGE", 
                      "PLACE", "HANDID", "NEWLINE", "INT" ]

    RULE_ts = 0
    RULE_title = 1
    RULE_description = 2
    RULE_buyin = 3
    RULE_players = 4
    RULE_prizepool = 5
    RULE_datetime = 6
    RULE_results = 7
    RULE_playerlist = 8
    RULE_player = 9
    RULE_prize = 10
    RULE_personal = 11

    ruleNames =  [ "ts", "title", "description", "buyin", "players", "prizepool", 
                   "datetime", "results", "playerlist", "player", "prize", 
                   "personal" ]

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
    T__13=14
    TSNAME=15
    TID=16
    GAME=17
    BUYIN=18
    MONEY=19
    CURSIGN=20
    CUR=21
    PLAYERNUM=22
    DATE=23
    RESULT=24
    NICKNAME=25
    LOCATION=26
    PERCENTAGE=27
    PLACE=28
    HANDID=29
    NEWLINE=30
    INT=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class TsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def title(self):
            return self.getTypedRuleContext(TournamentSummaryParser.TitleContext,0)


        def description(self):
            return self.getTypedRuleContext(TournamentSummaryParser.DescriptionContext,0)


        def buyin(self):
            return self.getTypedRuleContext(TournamentSummaryParser.BuyinContext,0)


        def players(self):
            return self.getTypedRuleContext(TournamentSummaryParser.PlayersContext,0)


        def prizepool(self):
            return self.getTypedRuleContext(TournamentSummaryParser.PrizepoolContext,0)


        def datetime(self):
            return self.getTypedRuleContext(TournamentSummaryParser.DatetimeContext,0)


        def results(self):
            return self.getTypedRuleContext(TournamentSummaryParser.ResultsContext,0)


        def personal(self):
            return self.getTypedRuleContext(TournamentSummaryParser.PersonalContext,0)


        def getRuleIndex(self):
            return TournamentSummaryParser.RULE_ts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTs" ):
                listener.enterTs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTs" ):
                listener.exitTs(self)




    def ts(self):

        localctx = TournamentSummaryParser.TsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ts)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.title()
            self.state = 25
            self.description()
            self.state = 26
            self.buyin()
            self.state = 27
            self.players()
            self.state = 28
            self.prizepool()
            self.state = 29
            self.datetime()
            self.state = 30
            self.results()
            self.state = 31
            self.personal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TitleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TSNAME(self):
            return self.getToken(TournamentSummaryParser.TSNAME, 0)

        def TID(self):
            return self.getToken(TournamentSummaryParser.TID, 0)

        def GAME(self):
            return self.getToken(TournamentSummaryParser.GAME, 0)

        def BUYIN(self):
            return self.getToken(TournamentSummaryParser.BUYIN, 0)

        def getRuleIndex(self):
            return TournamentSummaryParser.RULE_title

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTitle" ):
                listener.enterTitle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTitle" ):
                listener.exitTitle(self)




    def title(self):

        localctx = TournamentSummaryParser.TitleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_title)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(TournamentSummaryParser.TSNAME)
            self.state = 34
            self.match(TournamentSummaryParser.TID)
            self.state = 35
            self.match(TournamentSummaryParser.GAME)
            self.state = 36
            self.match(TournamentSummaryParser.BUYIN)
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
            return self.getToken(TournamentSummaryParser.TID, 0)

        def GAME(self):
            return self.getToken(TournamentSummaryParser.GAME, 0)

        def getRuleIndex(self):
            return TournamentSummaryParser.RULE_description

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDescription" ):
                listener.enterDescription(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDescription" ):
                listener.exitDescription(self)




    def description(self):

        localctx = TournamentSummaryParser.DescriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_description)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(TournamentSummaryParser.T__0)
            self.state = 39
            self.match(TournamentSummaryParser.TID)
            self.state = 40
            self.match(TournamentSummaryParser.T__1)
            self.state = 41
            self.match(TournamentSummaryParser.GAME)
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

        def BUYIN(self):
            return self.getToken(TournamentSummaryParser.BUYIN, 0)

        def CUR(self):
            return self.getToken(TournamentSummaryParser.CUR, 0)

        def getRuleIndex(self):
            return TournamentSummaryParser.RULE_buyin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuyin" ):
                listener.enterBuyin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuyin" ):
                listener.exitBuyin(self)




    def buyin(self):

        localctx = TournamentSummaryParser.BuyinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_buyin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(TournamentSummaryParser.T__2)
            self.state = 44
            self.match(TournamentSummaryParser.BUYIN)
            self.state = 45
            self.match(TournamentSummaryParser.CUR)
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

        def PLAYERNUM(self):
            return self.getToken(TournamentSummaryParser.PLAYERNUM, 0)

        def getRuleIndex(self):
            return TournamentSummaryParser.RULE_players

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlayers" ):
                listener.enterPlayers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlayers" ):
                listener.exitPlayers(self)




    def players(self):

        localctx = TournamentSummaryParser.PlayersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_players)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(TournamentSummaryParser.PLAYERNUM)
            self.state = 48
            self.match(TournamentSummaryParser.T__3)
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
            return self.getToken(TournamentSummaryParser.MONEY, 0)

        def CUR(self):
            return self.getToken(TournamentSummaryParser.CUR, 0)

        def getRuleIndex(self):
            return TournamentSummaryParser.RULE_prizepool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrizepool" ):
                listener.enterPrizepool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrizepool" ):
                listener.exitPrizepool(self)




    def prizepool(self):

        localctx = TournamentSummaryParser.PrizepoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_prizepool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(TournamentSummaryParser.T__4)
            self.state = 51
            self.match(TournamentSummaryParser.MONEY)
            self.state = 52
            self.match(TournamentSummaryParser.CUR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DatetimeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATE(self):
            return self.getToken(TournamentSummaryParser.DATE, 0)

        def getRuleIndex(self):
            return TournamentSummaryParser.RULE_datetime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDatetime" ):
                listener.enterDatetime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDatetime" ):
                listener.exitDatetime(self)




    def datetime(self):

        localctx = TournamentSummaryParser.DatetimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_datetime)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(TournamentSummaryParser.T__5)
            self.state = 55
            self.match(TournamentSummaryParser.DATE)
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
            return self.getTypedRuleContext(TournamentSummaryParser.PlayerlistContext,0)


        def getRuleIndex(self):
            return TournamentSummaryParser.RULE_results

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResults" ):
                listener.enterResults(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResults" ):
                listener.exitResults(self)




    def results(self):

        localctx = TournamentSummaryParser.ResultsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_results)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
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
            return self.getTypedRuleContext(TournamentSummaryParser.PlayerContext,0)


        def playerlist(self):
            return self.getTypedRuleContext(TournamentSummaryParser.PlayerlistContext,0)


        def getRuleIndex(self):
            return TournamentSummaryParser.RULE_playerlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlayerlist" ):
                listener.enterPlayerlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlayerlist" ):
                listener.exitPlayerlist(self)




    def playerlist(self):

        localctx = TournamentSummaryParser.PlayerlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_playerlist)
        try:
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.player()
                self.state = 60
                self.playerlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
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

        def RESULT(self):
            return self.getToken(TournamentSummaryParser.RESULT, 0)

        def NICKNAME(self):
            return self.getToken(TournamentSummaryParser.NICKNAME, 0)

        def LOCATION(self):
            return self.getToken(TournamentSummaryParser.LOCATION, 0)

        def prize(self):
            return self.getTypedRuleContext(TournamentSummaryParser.PrizeContext,0)


        def getRuleIndex(self):
            return TournamentSummaryParser.RULE_player

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlayer" ):
                listener.enterPlayer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlayer" ):
                listener.exitPlayer(self)




    def player(self):

        localctx = TournamentSummaryParser.PlayerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_player)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(TournamentSummaryParser.RESULT)
            self.state = 66
            self.match(TournamentSummaryParser.T__6)
            self.state = 67
            self.match(TournamentSummaryParser.NICKNAME)
            self.state = 68
            self.match(TournamentSummaryParser.T__7)
            self.state = 69
            self.match(TournamentSummaryParser.LOCATION)
            self.state = 70
            self.match(TournamentSummaryParser.T__8)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TournamentSummaryParser.MONEY:
                self.state = 71
                self.prize()


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
            return self.getToken(TournamentSummaryParser.MONEY, 0)

        def PERCENTAGE(self):
            return self.getToken(TournamentSummaryParser.PERCENTAGE, 0)

        def getRuleIndex(self):
            return TournamentSummaryParser.RULE_prize

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrize" ):
                listener.enterPrize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrize" ):
                listener.exitPrize(self)




    def prize(self):

        localctx = TournamentSummaryParser.PrizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_prize)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(TournamentSummaryParser.MONEY)
            self.state = 75
            self.match(TournamentSummaryParser.T__7)
            self.state = 76
            self.match(TournamentSummaryParser.PERCENTAGE)
            self.state = 77
            self.match(TournamentSummaryParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PersonalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLACE(self):
            return self.getToken(TournamentSummaryParser.PLACE, 0)

        def HANDID(self):
            return self.getToken(TournamentSummaryParser.HANDID, 0)

        def getRuleIndex(self):
            return TournamentSummaryParser.RULE_personal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPersonal" ):
                listener.enterPersonal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPersonal" ):
                listener.exitPersonal(self)




    def personal(self):

        localctx = TournamentSummaryParser.PersonalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_personal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(TournamentSummaryParser.T__10)
            self.state = 80
            self.match(TournamentSummaryParser.PLACE)
            self.state = 81
            self.match(TournamentSummaryParser.T__11)
            self.state = 82
            self.match(TournamentSummaryParser.T__12)
            self.state = 83
            self.match(TournamentSummaryParser.HANDID)
            self.state = 84
            self.match(TournamentSummaryParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





