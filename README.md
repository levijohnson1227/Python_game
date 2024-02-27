# Overview

For this sprint my aim was to build a game similar to battleship that took in users ship coordinates and attack commands. I wanted the users moves to communicate over a network. Each player will
enteract with a command line interface and send the coordinates for their moves (X,Y). The communication between players is done using a TCP protocol and the port number 9999. The game will be locally hosted
and the Player one will initiate the game by starting the server component and the second player will start the client component. They then connect through the local host and the specified port number.
The main reason I wanted to focus on this was to have some real application of networking concepts.

[Software Demo Video](https://www.youtube.com/watch?v=z-2SK71_dwc)

# Network Communication

I used client/server architecture for my network communication.
TCP protocal was used for communication and port number 9999 was specified for the game
The messages displayed during the game was a X for your moves and O for opponents moves. The game board was submitted after each move.

# Development Environment

This software was developed in Visual Studio Code. The program was written in python using the threading and socket libraries to handle the network communication.

# Useful Websites

- [python](https://docs.python.org/3.6/library/socket.html)
- [Wikipedia](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)
- [Youtube](https://www.youtube.com/watch?v=YwWfKitB8aA)

# Future Work

- I would like to better improve the user interface. Creating a GUI with a personal board and an attack board.
- I would also like to add a chat function so players can communicate when playing.
- I also want to add loading animations so when waiting on the other player
