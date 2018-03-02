from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'
doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass
    
class Player(BasePlayer):
    q1 = models.IntegerField(label="Rate from 1 is the worst and 5 the best. How much do you like healthy food?",
        choices=[1, 3, 5], 
        widget=widgets.RadioSelectHorizontal,
    )

    q2 = models.CurrencyField(label="Randomly the player choose an option that represents money",
        choices=[
            [1, '$ 1'],
            [2, '$ 2 '],
            [3, '$ 3'],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

