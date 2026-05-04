import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "music_network.csv"
RESULTS_DIR = BASE_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True)

# Read dataset
data = pd.read_csv(DATA_PATH)

# Create directed graph
G = nx.DiGraph()

# Add edges with musical distance values
for _, row in data.iterrows():
    G.add_edge(row["source"], row["target"], weight=row["distance"])

# Define start and target songs
start_song = "Sweet Child O Mine"
target_song = "Every Breath You Take"

# Find optimal path using Dijkstra's algorithm
optimal_path = nx.shortest_path(
    G,
    source=start_song,
    target=target_song,
    weight="weight"
)

total_distance = nx.shortest_path_length(
    G,
    source=start_song,
    target=target_song,
    weight="weight"
)

# Print results
print("Optimal playlist transition:")
print(" -> ".join(optimal_path))

print("\nTotal musical distance:")
print(total_distance)

# Draw network
pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(12, 8))

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=3000,
    font_size=8,
    arrows=True
)

edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_size=8
)

plt.title("80s Rock Playlist Transition Network")
plt.savefig(RESULTS_DIR / "music_network_visualization.png", bbox_inches="tight")
plt.show()