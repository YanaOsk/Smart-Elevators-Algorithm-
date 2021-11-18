# Ex1

## Explanation of the problem: 
Lifts are not always efficient. There are lots of cases, where people stand and wait a long time for the elevator to reach them and in general for them to reach their destination.
We first researched a bit on the internet and found a lot of studies that investigate the problem and also those that try to give the solution, for example, the KONE company that invented smart elevators, or works of people that trying to understand or build the algorithm of elevators.

# From the previous assignment we recycle the sources we were impressed with:

1)KONE company: https: //www.mako.co.il/nexter-internet/innovation/Article-5a5a6e2fad3a861006.htm

2)Minimizing Elevation Waiting Times (Ido Greenberg ): https://idogreenberg.neocities.org/linked%20files/Articles/Elevators%20weighting%20time%20optimization.pdf

3)Project in Artificial Intelligence - The Smart Elevator by Yonatan Gat and Gal Eyal: https://www.cs.huji.ac.il/~ai/projects/2014/The_intelevator/files/report.pdf

## Our offline algorithm:

We will understand the problem - we accept all the calls and need to insert them efficiently, so that the waiting time from the moment the person presses the floor button until he reaches the destination will be the shortest time.
Our algorithm works on time, that is, we want to test how long it takes for one call to be made and at the same time we check how long it takes to make calls that are already inside the elevator. We compare the times and want to see where to put the reading. We will put the reading in the same elevator, where the time of the same reading will have the least effect on the amount of time of all the readings in the same elevator. And so basically the inlay of the elevator is done

## UML DIAGRAM
![UML class](https://user-images.githubusercontent.com/69717074/142421732-358ba57d-6684-4677-a292-c7db9d7ea08d.png)
