# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  main.py                                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: fcaval <fcaval@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/20 14:54:17 by fcaval          #+#    #+#               #
#  Updated: 2026/02/20 17:17:33 by fcaval          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AgressiveStrategy
from ex3.GameEngine import GameEngine


def main():
    print("\n=== DataDeck Game Engine ===\n")
    
# ************************************************************************* #
#                           Configuring Card                                #
# ************************************************************************* #

    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AgressiveStrategy()
    engine = GameEngine()

    engine.configure_engine(factory, strategy)
    print(f"Available types: {factory.get_supported_types()}")


if __name__ == "__main__":
    main()