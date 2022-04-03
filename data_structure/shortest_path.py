from collections import deque
from GraphNode import *


class StationNode:
    """Simple class representing subway station
    for finding shortest path by BFS"""
    
    def __init__(self, name):
        self.station_name = name
        self.adjacent_stations = []
        self.visited = False
        self.predecessor = None  ## for shortest path
        return
    
    def add_connection(self,
        other_station : Type['StationNode']
        ) -> None:
        """Save edge btw StationNodes"""
        self.adjacent_stations.append(other_station)
        other_station.adjacent_stations.append(self)
        return

    def __str__(self) -> str:
        """Print string for StationNode"""
        res_str = f'{self.station_name}: '
        
        for station in self.adjacent_stations:
            res_str += f'{station.station_name} '
            
        return res_str
 

def bfs(
    graph : Dict[str, StationNode],
    start_node : StationNode
    ) -> None:
    
    """BFS for finding shortest path"""
    
    ## init all StationNode in graph
    for station in graph.values():
        station.visited = False
        station.predecessor = None
    
    ## BFS
    queue = deque()
    start_node.visited = True
    queue.append(start_node)
    while queue:
        current_node = queue.popleft()
        for neighbor_node in current_node.adjacent_stations:
            if not neighbor_node.visited:
                neighbor_node.visited = True
                neighbor_node.predecessor = current_node
                queue.append(neighbor_node)
    return

def back_track(destination_node : StationNode) -> str:
    """Back-tracking from destination_node to start_node"""
    
    shortest_path = ''
    current_node = destination_node
    while current_node:
        shortest_path = f'{current_node.station_name} {shortest_path}'
        current_node = current_node.predecessor
    return shortest_path


if __name__ == '__main__':
    
    ## test bfs for shortest path
    stations = create_subway_graph("./algorithm/data_structure/new_stations.txt")  # stations.txt 파일로 그래프를 만든다
    bfs(stations, stations['을지로3가'])
    print(back_track(stations['강동구청']))