from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = """
This is a one-period public goods game with 2 players.
"""

class Constants(BaseConstants):
    name_in_url = 'taxes2'
    players_per_group = 2
    num_rounds = 2

    instructions_template = 'taxes2/Instructions.html'

    # """Amount allocated to each player"""
    endowment = c(100)
    multiplier = 1


class Subsession(BaseSubsession):
    def vars_for_admin_report(self):
        ideclarado = [p.ideclarado for p in self.get_players() if p.ideclarado != None]
        if ideclarado:
            return {
                'avg_ideclarado': sum(ideclarado)/len(ideclarado),
                'min_ideclarado': min(ideclarado),
                'max_ideclarado': max(ideclarado),
            }
        else:
            return {
                'avg_ideclarado': '(no data)',
                'min_ideclarado': '(no data)',
                'max_ideclarado': '(no data)',
            }


class Group(BaseGroup):
    total_ideclarado = models.CurrencyField()

    individual_share = models.CurrencyField()

    def set_payoffs(self):
        self.total_ideclarado = sum([p.ideclarado for p in self.get_players()])
        self.individual_share = self.total_ideclarado * Constants.multiplier / Constants.players_per_group
        for p in self.get_players():
            p.payoff = (Constants.endowment - 0.28*p.ideclarado)


class Player(BasePlayer):
    ideclarado = models.CurrencyField(
        min=0, max=100,
        doc="""Monto declarado por el participante""",
    )

