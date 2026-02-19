# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  EliteCard.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/19 16:52:15 by fcaval          #+#    #+#               #
#  Updated: 2026/02/19 17:03:08 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex0.Card import Card
from abc import ABC, abstractmethod
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    
    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target) -> dict:
        pass

    def defend(self, incoming_damage: int) -> dict:
        pass

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        pass

    def get_magic_stats(self) -> dict:
        pass

    def channel_mana(self, amount: int) -> dict:
        pass
    
    
