# Engine Generator

## What is Engine Generator?
Engine Generator is a peice of software that is inteded to generate engines for Ange Yaghi's Engine Simulator program. The main idea beging it, is the fact that Ange's Engine Simulator uses thir own custom programming language they created, called parahna, and while it is simmilar to python or C based languages, it can still take some time to get used to, expeshally if you do not fully undetstand how engines work in the first place. The program is intended to be used by those who know more about the inner workings of engines, and cars in generel, however it may be usesful to those who know little to nothing about cars, in helping them learn how internal combustion engines work.

## What is the current state of Engine Generator?
It was originally developed by Ange as a project for a youtube video, to help them create various engine designs, but was quickly abandoned and never inteded to be updated. Its development has been taken up by me (hackall360) and is currently in the process of being re-written to have better usability by the end user.

## What does Engine Generator do?
The main functionality of Engine Generator, is to generate engines for engine simulator, in a way that requires zero programming. Initally the engine generator would require sombody program out specific values for the engine, and pipe them into a function that can generate a specific engine, and I saw an opportunity to expand on that functionality and have a program sit there and ask a user for values that it uses in its engine generation.

## Will you contenue to update the Engine Generator?
For the time being, I plan on updating the engine generator as it needs to be updated, either for the game updating or for features the community wants, however I will not be updating this indefinitely, as I am using my spare time to work on the engine generator, and my interist can shift drastically to another project. I will say that once Ange has released the engine simulator in full on steam, I will more than likely stop working on the engine generator entirely, as once Ange has released the engine simulator, there will be many more tools available inside the engine simulator, including talk of a 3D editor, and support for exporting to automation or BeamNG. The engine simulator at that point, will also have so much added functionality, that the entire engine generator will require a full re-write yet again.

## How to use Engine Generator?
There are two ways to use Engine Generator currently, either you can run the script directly, or you can download the executable binary file and use that. Either way you should be running the same exact code that will generate an engine.
### Running the script
- Ensure you have python 3 installed properly. If you do not have python installed, you will need to install python from this website [Python Download](https://www.python.org/downloads/)
- Open a console window / terminal window and run the command `py engine.py` to start generating the engine
- Follow the on-screen instructions to generate the engine to parameters
- One the program has exited, you should have a new .mr file in your current directory, this is your engine
- Open engine simulator, and load your engine
### Running the executable binary
- Download the executable binary from the releases page
- Run the executable binary
- Follow the on-screen instructions to generate the engine to parameters
- One the program has exited, you should have a new .mr file in your current directory, this is your engine
- Open engine simulator, and load your engine

## This script is no-longer garbage