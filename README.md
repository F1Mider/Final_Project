# Title: CBP Airport Waiting Time

## Team Member(s): Haocong Cheng

# Monte Carlo Simulation Scenario & Purpose:

The initial idea comes when I have to decide which shuttle bus I should take after arriving in Chicago in August (I
haven’t decided yet but got a preference). When looking for some clues, I found the website (https://awt.cbp.gov/)
hosted directly by U.S. Customs and Border Protection (CBP) that has waiting time by flight arrival time (in each hour)
in major airports. The data are recorded since July 2008, so there should be decent amount of data to go through.

This model is able to take a given flight schedule of any airport on a day, together with the number of booths opened
during each hour. It can then simulate the immigration area of this airport of the day and generate report of waiting
times of each passenger. The statistics are similar to the ones retrieved from CBP website.

The model can then be used to answer questions like if an airport is adding an international flight at this time, how
much longer will passengers clear the line. It can also be used to find how many booths is needed to clear people
effectively in peak seasons.


## Simulation's variables of uncertainty

There are currently two random variables. One is the proportion of U.S. citizens vs non-U,S. citizens, and the other is
the processing time of each passenger (different for citizens vs non-citizens. Both variables are not specified by the
dataset by CBP, and the time are generated based on predicted normal distribution models.

For the proportion of citizens, the mean is 0.6 and the standard deviation is 0.1. While this distribution is only
proposed, it seems like based on dataset for August 2nd, the ratio is close to this model. The distribution can be
improved after analyzing more real data.

For the processing time, there is less clue to predict. The time for non-citizen is based on my own experiences, but
the distribution might be skewed to the right since there are cases when passengers take longer to clear the process.
These distributions can be adjusted to get the result close to the real data.

## Hypothesis or hypotheses before running the simulation:
The hypothesis is that by changing the ratio of booths for citizens vs non-citizens, and time to process each person,
the result should be similar to the real data provided by CBP.

## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?
What are the management decisions one could make from your simulation's output, etc.)

There are several factors that are not considered in this model, and thus generating differences from real data.

First, the passengers from the next flight is queued after the previous flight. In the real world, it takes longer
for the last row to get off the plane. Therefore, the queue will be mixed with passengers from several flights.

Second, with the presence of automated systems, many passengers should be using that instead of going through the booth.
This factor is not yet considered. Therefore, in peak hours, no passenger can get through the line within 15 minutes.
In the real world, there are passengers who can do so.

Third, there are cases when some citizens are queueing together with non-citizens. For example, with two passengers
travelling together, they might stay in the same line for non-citizen despite one of them can wait on the citizens'
side. This could explain the similar numbers observed in maximum waiting time.

It turned out that with the predicted processing time and proportion of booths, the waiting time is less than real data
during off-peak hours, and longer in peak hours. The line, especially the non-citizen one, tend to pile up when a
significant amount of flights arrive.

There are a few ways to improve this program. For example, add a third line for Global Entry passengers, automatically
control number of booths, randomly pause a booth for a few minutes, and some other factors discussed earlier.


## Instructions on how to use the program:
Basically just run the program and the data will generate. To change the flight schedule, unfortunately the only way
to do so is by manually input flight information(time arrived and passengers on board). To change the opened booths at
each hour, it will be the second function with first number in each list number of booths for citizens, and the second
one for non-citizens. The total number of booths is defind in main function and is currently 30.

To change the distribution of random variables, look for np.random.normal() function, and change the mean and standard
deviation accordingly. Note that it is easy to pile up the non-citizens even by adding the mean of processing time by
just 0.1.

## All Sources Used:
https://awt.cbp.gov
https://www.airport-ohare.com/arrivals-terminal-5