# Ericsson-5G-2D-positioning-estimation-system-Arctic-Challenge-Hackathon
5G and Beyond communication is key to the digitalization of industries and for Industry. In industry and manufacturing scenarios, positioning is also an important functionality, with use cases such as inventory and supply management (supervision of the flow of materials and goods), monitoring of tools in manufacturing floors, operating automatic guided vehicles (AGVs), safety (in scenarios where humans are working close to machines), personnel tracking in mines, etc. Most of these use cases require accurate positioning. 
In this challenge, which is about 2D positioning, you will estimate the 2D (x, y) position at every time instant using noisy time-difference-of-arrival (TDoA) measurements obtained with 7 base stations. For ideal TDoA measurements, the position at every time instant is obtained as the intersections of the hyperbolas formed by the TDoAs. For noisy measurements however, the hyperbolas will not intersect.  You will therefore design an accurate least squares method to estimation the positions.

Given the time-of-arrival (ToA) measurements and base station (BS) positions shown in figure 1 below, you will:
•	Compute the TDoAs by considering one of the BS as the reference and then derive a simple least squares method to estimate the position. 
•	Additionally, you will visualise the output (estimated positions at every time instant) together with the BS locations.

The data required to carry out this task is provided in 2 different formats to allow selection depending on the tools to use for this task. 
1.	A MATLAB file (structure) which contains 2 fields for the ToA measurements and base station positions.
2.	Two csv files for the ToA measurements and base station positions.
For each of the data formats:
	The ToA measurements (in seconds) are provided in a matrix of   T = 304 rows and N_BS = 7 columns. For example, the 1st row of this matrix contains the ToA
measurements collected at time instant 1 for all the seven base stations.

	The 2D base station locations are also provided in another matrix of T = 2 rows and N_BS = 7 columns, where each column is the (x, y)-coordinate of each base station.
