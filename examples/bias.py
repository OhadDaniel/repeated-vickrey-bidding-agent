import random
from typing import Dict, List


class BiddingAgent:
    """Truthful bidding strategy with time-varying random shading"""

    TOTAL_ROUNDS = 15

    def __init__(self, team_id: str, valuation_vector: Dict[str, float],
                 budget: float, opponent_teams: List[str]):
        self.team_id = team_id
        self.valuation_vector = valuation_vector
        self.budget = float(budget)
        self.initial_budget = float(budget)
        self.opponent_teams = opponent_teams
        self.utility = 0.0
        self.items_won = []
        self.rounds_completed = 0  #

    def _update_available_budget(self, item_id: str, winning_team: str, price_paid: float):
        if winning_team == self.team_id:
            self.budget -= float(price_paid)
            self.items_won.append(item_id)

    def update_after_each_round(self, item_id: str, winning_team: str, price_paid: float):
        self._update_available_budget(item_id, winning_team, price_paid)
        if winning_team == self.team_id:
            self.utility += (float(self.valuation_vector[item_id]) - float(price_paid))

        self.rounds_completed += 1
        return True

    def rand_multiplier(self) -> float:
        r = self.rounds_completed  # 0-based:

        # 0-5
        if r <= 5:
            lo, hi = 0.85, 0.9
        # 6-10
        elif r <= 10:
            lo, hi = 0.9, 0.95
        # 11 -14
        else:
            lo, hi = 0.95, 0.98

        return random.uniform(lo, hi)

    def bidding_function(self, item_id: str) -> float:
        v = float(self.valuation_vector.get(item_id, 0.0))
        if v <= 0.0 or self.budget <= 0.0:
            return 0.0

        num = self.rand_multiplier()

        EPS = 1e-6
        bid = v * num

        # avoid engine cap warnings due to float
        bid = min(bid, max(0.0, self.budget - EPS))
        return max(0.0, bid)