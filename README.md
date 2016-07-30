# This bus goes round the houses!

Late teens growing up in the suburbs of London meant relying on buses because it was not cool to cycle or walk anywhere. It took ages just to go a few miles down the round.

Now, years later and with some knowledge of Python I can finally verify if the bus I relied on did indeed go round the houses.

Using busroute data from TfL (bus-sequences.csv) and some Python goodies this is my attempt.

The approach is to chuck all the data into geopandas, calculate the length of a route as a Line and then substract the distance between the start and end point. The bus that goes round the houses will be the one with where this difference is the greatest.




