Documentation
=============

At this point in time the package contains three primary classes and two child classes which will are documented in this section.

Player
******

A player class used to represent any sports team/person that will go onto compete in competitions of a classic 1v1 elemination tournament.

.. py:class:: player(skill,variance,name)

   The class that is used to represent a player/team

   :param int skill: The underlying skill level that this player has.
   :param int variance: The variance that this player has whenever they perform, the smaller this is the more consistent they are.
   :param str name: The name/id for the player which can be used as a reference.

   :var int skill: The skill of the player assigned upon construction.
   :var int variance: The variance of the player assigned upon construction.
   :var str name: The skill of the player assigned upon construction.
   :var list(int) pointRec: A list of the points that a player has earnt from competing in tournaments.
   :var int totalPoints: The total value of all the points contained in pointRec.


   .. py:classmethod:: perform()

      A method that gets the player to perform and returning a integer value to represent the performance 'on the day'.

      :returns performance: a rounded int that has been sampled from a normal dist. characterised by the players skill and variance.
      :rtype: int


   .. py:classmethod:: selfsummary()

      A method that prints a quick summary of the players variable.

      :returns: printed string
      :rtype: none

   .. py:classmethod:: gainPoints(points)

      A method to add the given points to the players point record.
      If this now contains more than 10 entries it will remove the first record and then update the totalPoints variable with the sum of the list.

      :var int points: The points that are to be added to the players record.
      :rtype: none 

Tournaments
***********

Seasons
*******
