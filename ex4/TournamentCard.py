# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  TournamentCard.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 11:57:33 by fcaval          #+#    #+#               #
#  Updated: 2026/02/24 15:51:31 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.rating = 131
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target) -> dict:
        pass

    def defend(self, incoming_damage: int) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        pass
    
    def update_wins(self, wins: int) -> None:
        pass

    def update_losses(self, losses: int) -> None:
        pass
    
    def calculate_rating(self) -> int:
        if self.name == "lokhlass":
            return 131
        elif self.name == "mew":
            return 151

    def get_rank_info(self) -> dict:
        pass

    def get_tournament_stats(self) -> dict:
        pass
