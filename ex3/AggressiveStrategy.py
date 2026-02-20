# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  AggressiveStrategy.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 14:46:11 by fcaval          #+#    #+#               #
#  Updated: 2026/02/20 17:09:36 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.GameStrategy import GameStrategy

class AgressiveStrategy(GameStrategy):

    def __init__(self):
        self.name = "AgressiveStrategy"

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        pass

    def get_strategy_name(self) -> str:
        pass

    def prioritize_targets(self, available_targets: list) -> list:
        pass
