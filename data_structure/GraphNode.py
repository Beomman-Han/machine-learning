from collections import deque
from typing import Dict, Literal, Type


class StationNode:
    """Simple class representing subway station"""
    
    def __init__(self, name):
        self.station_name = name
        self.adjacent_stations = []
        self.visited : Literal[0, 1, 2] = 0  ## 0, 1, 2
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
        
        
def create_station_nodes(
    input_file: str
    ) -> Dict[str, StationNode]:
    """Return dict of StationNode from input file"""
    
    stations = dict()
    f = open(input_file, 'r')
    for line in f:
        for name in line.strip('\n').split(' - '):
            station = StationNode(name)
            if name not in stations.keys():
                stations[name] = station
    f.close()
    
    return stations

def create_subway_graph(input_file):
    
    stations = dict()
    f = open(input_file, 'r')
    for line in f:
        names = [ x.strip() for x in line.strip('\n').split(' - ') ]
        
        if names[0] not in stations.keys():
            stations[names[0]] = StationNode(names[0])

        for i in range(1, len(names)):
            if names[i] not in stations.keys():
                station = StationNode(names[i])
                station.add_connection(stations[names[i-1]])
                stations[names[i]] = station
            else:
                station = stations[names[i]]
                station.add_connection(stations[names[i-1]])
    f.close()
    
    return stations

def bfs(
    graph : Dict[str, StationNode],
    start_node : StationNode
    ) -> None:
    
    """Visit every node which could go from start_node, breadth first.
    
    1) append node to queue
    2) while queue empty,
        - pop node
        - for every connected node,
            - if not visited, visit
            - append every connected node
    """
    
    queue = deque()
    
    for station_node in graph.values():
        station_node.visited = False
    
    start_node.visited = True
    queue.append(start_node)
    
    while len(queue) != 0:
        station = queue.popleft()
        for adj_station in station.adjacent_stations:
            if not adj_station.visited:
                adj_station.visited = True
                queue.append(adj_station)

    return

def dfs(
    graph : Dict[str, StationNode],
    start_node : StationNode
    ) -> None:
    
    """Search every node from start_node, depth first"""
    
    for station in graph.values():
        station.visited = 0
    
    stack = deque()
    start_node.visited = 1
    stack.append(start_node)
    
    while stack:
        top_node = stack.pop()
        top_node.visited = 2
        
        for neighbor in top_node.adjacent_stations:
            if not neighbor.visited:
                neighbor.visited = 1
                stack.append(neighbor)

    return

    
if __name__ == '__main__':
    ## Init instance for subway station
    # station_0 = StationNode('교대역')
    # station_1 = StationNode('사당역')
    # station_2 = StationNode('종로3가역')
    # station_3 = StationNode('서울역')
    
    ## Save StationNodes to python list
    # stations = [station_0, station_1, station_2, station_3]
    
    ## Save StationNodes to python dict
    # stations = {
    #     '교대역': station_0,
    #     '사당역': station_1,
    #     '종로3가역': station_2,
    #     '서울역': station_3
    # }
    
    ## test create_station_nodes function
    # stations = create_station_nodes("./algorithm/data_structure/stations.txt")  # stations.txt 파일로 그래프 노드들을 만든다
    ## print name of station in stations
    # for station in sorted(stations.keys()):
    #     print(stations[station].station_name)
    
    # stations = create_subway_graph("./algorithm/data_structure/stations.txt")  # stations.txt 파일로 그래프를 만든다
    # ## print adjacent list of station in stations
    # for station in sorted(stations.keys()):
    #     print(stations[station])

    ## test bfs function
    # stations = create_subway_graph("./algorithm/data_structure/new_stations.txt")  # stations.txt 파일로 그래프를 만든다
    stations = create_subway_graph('./new_stations.txt')

    gangnam_station = stations["강남"]

    # # 강남역과 경로를 통해 연결된 모든 노드를 탐색
    # bfs(stations, gangnam_station)

    # # 강남역과 서울 지하철 역들이 연결됐는지 확인
    # print(stations["강동구청"].visited)
    # print(stations["평촌"].visited)
    # print(stations["송도"].visited)
    # print(stations["개화산"].visited)

    # # 강남역과 대전 지하철 역들이 연결됐는지 확인
    # print(stations["반석"].visited)
    # print(stations["지족"].visited)
    # print(stations["노은"].visited)
    # print(stations["(대전)신흥"].visited)
    
    # 강남역과 경로를 통해 연결된 모든 노드를 탐색
    dfs(stations, gangnam_station)

    # 강남역과 서울 지하철 역들이 연결됐는지 확인
    print(stations["강동구청"].visited)
    print(stations["평촌"].visited)
    print(stations["송도"].visited)
    print(stations["개화산"].visited)

    # 강남역과 대전 지하철 역들이 연결됐는지 확인
    print(stations["반석"].visited)
    print(stations["지족"].visited)
    print(stations["노은"].visited)
    print(stations["(대전)신흥"].visited)