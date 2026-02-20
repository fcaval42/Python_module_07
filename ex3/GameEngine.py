# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  GameEngine.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 14:51:41 by fcaval          #+#    #+#               #
#  Updated: 2026/02/20 17:07:57 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    
    def __init__(self):
        self.factory= None
        self.strategy = None

    def configure_engine(self, factory: CardFactory, 
                         strategy: GameStrategy) -> None:
        self.factory = factory
        print(f"Factory: {self.factory.name}")
        self.strategy = strategy
        print(f"Strategy: {self.strategy.name}")

    def simulate_turn(self) -> dict:
        pass

    def get_engine_status(self) -> dict:
        pass
