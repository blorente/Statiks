from TournamentSummaryListener import TournamentSummaryListener

class TSParser(TournamentSummaryListener):
    def enterBuyin(self, ctx):
        print('Buyin: ' + str(ctx.BUYIN()))
