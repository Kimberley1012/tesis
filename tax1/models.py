from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BasePlayer,
    Currency as c, currency_range
)
import random

doc = """
This is a one-period public goods game with 2 players.
"""


class Constants(BaseConstants):
    name_in_url = 'tax1'
    players_per_group = 1
    num_rounds = 3

    instructions_template = 'tax1/Instructions.html'

    # """Amount allocated to each player"""
    endowment = c(15)
    multiplier = 1


class Subsession(BaseSubsession):
    def vars_for_admin_report(self):
        contributions = [p.contribution for p in self.get_players() if p.contribution != None]
        if contributions:
            return {
                'avg_contribution': sum(contributions)/len(contributions),
                'min_contribution': min(contributions),
                'max_contribution': max(contributions),
            }
        else:
            return {
                'avg_contribution': '(no data)',
                'min_contribution': '(no data)',
                'max_contribution': '(no data)',
            }

class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, max=3,
        doc="""The amount contributed by the player""",
    )
    def set_payoffs(self):
        for p in self.get_players():
            p.payoff = Constants.endowment - p.contribution