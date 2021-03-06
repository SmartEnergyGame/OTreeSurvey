from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = models.Player
    form_fields = ['q1', 'q2']

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass

class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        self.player.participant.vars['round1'] = sum([p.q2 for p in self.player.in_all_rounds()])
        return {
            'total': sum([p.q2 for p in self.player.in_all_rounds()]),
        }

page_sequence = [
    MyPage,
    ResultsWaitPage,
    Results
]
