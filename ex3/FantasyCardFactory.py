# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  FantasyCardFactory.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 14:48:20 by fcaval          #+#    #+#               #
#  Updated: 2026/02/20 17:29:58 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.CardFactory import CardFactory
from ex0.Card import Card

class FantasyCardFactory(CardFactory):

    data = {
        "creatures"#en cours, il faut faire de la data pour pouvoir piocher 
    }

    def __init__(self):
        self.name = "FantasyCardFactory"

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        pass

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

    def create_themed_deck(self, size: int) -> dict:
        pass

    def get_supported_types(self) -> dict:
        