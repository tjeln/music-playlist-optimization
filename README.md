# 80s Rock Playlist Transition Optimization

## Project Overview
This project applies network optimization to a music playlist recommendation problem. The main objective is to find the smoothest transition path between selected 1980s rock songs.

In this project, songs are modeled as nodes in a directed graph, and possible transitions between songs are modeled as edges. Each edge has a musical distance value. A lower distance value means that the transition between two songs is smoother and more compatible.

## Problem Description
Music streaming platforms often recommend songs based on similarity in genre, tempo, energy, mood, and overall listening experience. This project simulates a simplified version of that recommendation logic.

The goal is to find the optimal playlist transition from:

**Sweet Child O Mine**

to:

**Every Breath You Take**

by minimizing the total musical distance.

## Network Model
The project is modeled as a graph-based network optimization problem.

- **Nodes:** 1980s rock songs
- **Edges:** Possible transitions between songs
- **Weights:** Musical distance scores

A smaller weight indicates a smoother transition, while a larger weight indicates a less compatible transition.

## Dataset
The dataset is stored in:

```text
data/music_network.csv
```

Each row in the dataset represents a possible transition between two songs.

The columns are:

- `source`: starting song
- `target`: next song
- `distance`: musical distance between the two songs

The distance values were manually assigned based on general musical similarity, including genre, energy, tempo, and overall listening flow.

## Algorithm Used
This project uses **Dijkstra’s Shortest Path Algorithm**.

Dijkstra’s algorithm is suitable for this project because the goal is to find the path with the minimum total weight from a starting node to a target node.

In this project:

- shortest path = smoothest playlist transition
- edge weight = musical distance
- minimum total distance = most compatible song sequence

## Results
The algorithm found the following optimal playlist transition:

```text
Sweet Child O Mine → Eye of the Tiger → Every Breath You Take
```

The total musical distance is:

```text
7
```

This means that, according to the defined distance values, this sequence provides the smoothest transition from the starting song to the target song.

## Visualization
The project also generates a network visualization that shows the relationships between songs and their transition weights.

The generated image is saved in:

```text
results/music_network_visualization.png
```

This visualization helps explain how the songs are connected and how the algorithm selects the optimal route.

## Managerial Interpretation
This project demonstrates how network optimization can be applied to music recommendation systems. A similar approach could be used by platforms such as Spotify, Apple Music, or YouTube Music to create smoother playlists.

By minimizing musical distance, streaming platforms can:

- improve playlist quality
- increase user satisfaction
- create smoother listening experiences
- support automated recommendation systems

## Technologies Used
- Python
- pandas
- NetworkX
- matplotlib

## Project Structure

```text
music-playlist-optimization/
│
├── data/
│   └── music_network.csv
│
├── src/
│   └── solution.py
│
├── results/
│   └── music_network_visualization.png
│
├── notebooks/
│   └── analysis.ipynb
│
├── README.md
└── requirements.txt
```

## How to Run the Project

First, install the required libraries:

```bash
pip install -r requirements.txt
```

Then run the Python script:

```bash
python src/solution.py
```

If the command above does not work on Windows, try:

```bash
py src/solution.py
```

Make sure you run the command from the project root folder.

## Expected Output
After running the project, the terminal should display an output similar to:

```text
Optimal playlist transition:
Sweet Child O Mine -> Eye of the Tiger -> Every Breath You Take

Total musical distance:
7
```

The visualization file will also be created or updated in the `results` folder.

## Conclusion
This project shows that a music playlist recommendation problem can be represented as a network optimization problem. By using Dijkstra’s Shortest Path Algorithm, the system identifies the playlist path with the lowest total musical distance.

Although the dataset is manually created for educational purposes, the same method can be extended with real music data such as tempo, energy, danceability, and genre similarity.
