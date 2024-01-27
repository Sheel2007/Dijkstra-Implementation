# Dijkstra's Implementation

## Overview

This repository contains the code for an Artificial Intelligence Program that can get through a maze. The AI utilizes Dijktra's pathfinding algorithm to find the shortest way to get through a maze. 

## Usage 🚀

```
git clone https://github.com/Sheel2007/Dijkstra-Implementation
cd Dijkstra-Implementation
pip3 install -r requirements.txt
python3 ai_pathfinding.py
```
Note: If the commands pip3 and python3 do not work use the commands pip and python respectively:

```
pip install -r requirements.txt
python ai_pathfinding.py
```

## Preview 🔎

The program will begin from the end point and calculate backward the shortest possible moves to reach the start point. As it goes from node to node the tiles will turn from white to gray, which indicates the program has accounted for that node. Once it is finished, the program will draw the path from the start node to the end node.

<img src="images/preview.png" alt="Preview Image" width="800"/>

## Customization 

In order to change the barriers of and start and end points of the maze, you will need to change the `self.internal_map` variable that starts on line 20.

### Color Code:

Each number in the array `self.internal_map` represents something different:

| Number | Color     | Meaning                           |
|--------|-----------|-----------------------------------|
| 0      | White     | Tile that the AI can traverse     |
| 1      | Red       | Barrier that the AI must go around|
| 2      | Green     | Endpoint that the AI must reach   |
| 3      | Blue      | Start point for the path          |
