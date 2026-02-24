# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 12:02:26 by fcaval          #+#    #+#               #
#  Updated: 2026/02/24 16:44:02 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    
    print("\n=== DataDeck Tournament Platform ===\n")
    
    print("Registering Tournament Cards...\n")

    plateform = TournamentPlatform()

# ************************************************************************* #
#                             First pokemon                                 #
# ************************************************************************* #

    lokhlass = TournamentCard("lokhlass", 1, "Shiny", 20, 100)
    id_name = plateform.register_card(lokhlass)

    print(f"{lokhlass.name} ({id_name})")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {lokhlass.calculate_rating()}")
    print(f"- Record: {lokhlass.wins}-{lokhlass.losses}")
    print()

# ************************************************************************* #
#                            Second pokemon                                 #
# ************************************************************************* #

    mew = TournamentCard("mew", 1, "Immersive", 30, 80)
    id_name = plateform.register_card(mew)

    print(f"{mew.name} ({id_name})")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {mew.calculate_rating()}")
    print(f"- Record: {mew.wins}-{mew.losses}")




if __name__ == "__main__":
    main()