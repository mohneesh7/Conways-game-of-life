# <center>Conway's Way of Life<center>
********
**Rules:**
----

The universe is a finite two dimensional grid of square cells (square matrix). Each cell has 2 possible states, alive or dead. Every cell interacts with its neighbors, these cells are horizontal, vertical, diagonal or adjacent. herefore, each cell can have up to eight neighbors.At each step in time, the following transitions occur:

*  Any live cell with fewer than two live neighbors dies, because of under
population.
* Any live cell with two or three live neighbors, lives on to the next generation.
* Any live cell with more than three live neighbors dies, because of overpopulation.
* Any dead cell with exactly three live neighbors becomes a live cell, because of
reproduction.

## How to run the code:
---
1. Install _numpy :_

		C:\>pip install numpy
2. Give input as a text file.
	
	__The matrix should be NxN__
3. Sample input command :
	
		C:\Users\Mohneesh\Desktop\Assignment>wayoflife_mohneesh.py -f matrix.txt
__or__  	
		
		C:\Users\Mohneesh\Desktop\Assignment>wayoflife_mohneesh.py --file matrix.txt
## Visualizing More Than One Generation

**Simply modify the number of generations you want in the for loop at line 54**


## Inputs and Expected Outputs

#### input 1						
**010**  
**111**  
**010** 

#### output 1
**111**  
**101**  
**111**

#### input 2
**00000**  
**01110**  
**01110**  
**01110**  
**00000**  

#### output 2
**00100**  
**01010**  
**10001**  
**01010**  
**00100**  
