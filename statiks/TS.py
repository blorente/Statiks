from .grammars.TSParserListener import TSParserListener

class TS(TSParserListener):
    def exitBuyin(self, ctx):
        print('Buyin: ' + str(ctx.cost.MONEY(0)))
