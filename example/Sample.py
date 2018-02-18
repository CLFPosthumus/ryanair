#!/usr/bin/env python
from ryanair import Ryanair,departuredates, returndates

ryanair = Ryanair()

#Find departure flights
departureflights = ryanair.flights(departuredates,outputfile='Departure.xlsx')

#Find return flights. This inverses the departure/arrival airports.
returnflights = ryanair.flights(returndates,outputfile='Return.xlsx',returnflight= True)

#Find round flights, based on the previous output
roundflights = ryanair.roundflights(departureflights,returnflights,outputfile = 'Round.xlsx')


print('Sample script has finished')