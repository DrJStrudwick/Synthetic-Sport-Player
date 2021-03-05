Documentation
=============

At this point in time the package contains four primary classes and two child classes which will are documented in this section.

Player
******

A player class used to represent any sports team/person that will go onto compete in competitions of a classic 1v1 elemination tournament.

.. autoclass:: synthSportPlayer.player
   :members:
   :undoc-members:

Match
*****

A match class to represent to represent two players competing against each other where one will win and the other loses.

.. autoclass:: synthSportPlayer.match
   :members:
   :undoc-members:


Tournaments
***********

A class that represents a 1v1 elimination tournament that a collection of players enter and then proceed to compete until there is only one player who has won it all.

.. autoclass:: synthSportPlayer.tournament
   :members:
   :undoc-members:
   
.. autoclass:: synthSportPlayer.liveTourn
   :members:
   :undoc-members:
   :show-inheritance:

Seasons
*******

A class the represents a season, which is in essence a sequence of tournaments where the players play one after another and collect points based on how far they got. 

.. autoclass:: synthSportPlayer.season
   :members:
   :undoc-members:
   
.. autoclass:: synthSportPlayer.liveSeason
   :members:
   :undoc-members:
   :show-inheritance:
