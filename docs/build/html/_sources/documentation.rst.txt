Documentation
=============

At this point in time the package contains four primary classes and two child classes which will are documented in this section.

Player
******

A player class used to represent any sports team/person that will go onto compete in competitions of a classic 1v1 elemination tournament. A subclass :py:class:`bye` exists to models byes, for the situations where there are not enough players for the format and so byes can be added.

.. autoclass:: synthSportPlayer.player
   :members:
   :undoc-members:

.. autoclass:: synthSportPlayer.bye
   :members:
   :undoc-members:
   :show-inheritance:

Match
*****

A match class to represent to represent two players competing against each other where one will win and the other loses.

.. autoclass:: synthSportPlayer.match
   :members:
   :undoc-members:


Tournaments
***********

Classes that represents a tournament that a collection of players enter and then proceed to compete until there is only one player who has won it all. Here we have two main classes :py:class:`tournament` which model 1v1 elimination tournaments. the other :py:class:`robin` which models Round bin tournaments. 

.. autoclass:: synthSportPlayer.tournament
   :members:
   :undoc-members:
   
.. autoclass:: synthSportPlayer.liveTourn
   :members:
   :undoc-members:
   :show-inheritance:
   
.. autoclass:: synthSportPlayer.robin
   :members:
   :undoc-members:

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

Ultilities
**********

These functions are ultility functions designed to help with any analysis to be done.

.. autofunction:: synthSportPlayer.generatePlayers

.. autofunction:: synthSportPlayer.fetchPlayerSummary

.. autofunction:: synthSportPlayer.getPlayerHist

.. autofunction:: synthSportPlayer.getMatchUpData
