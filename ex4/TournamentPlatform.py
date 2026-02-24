# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  TournamentPlatform.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 12:00:32 by fcaval          #+#    #+#               #
#  Updated: 2026/02/24 15:36:12 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex4.TournamentCard import TournamentCard


class TournamentPlatform():

    def register_card(self, card: TournamentCard) -> str:
        lokhlass_id = 000
        mew_id = 000
        if card.name == "lokhlass":
            lokhlass_id += 1
            return f"ID: lokhlass_00{lokhlass_id}"
        elif card.name == "mew":
            mew_id += 1
            return f"ID: mew_00{mew_id}"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        pass

    def get_leaderboard(self) -> list:
        pass

    def generate_tournament_report(self) -> dict:
        pass
