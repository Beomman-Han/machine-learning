import sys
from typing import Dict, Type


class StationNode:
    """Simple class representing subway station"""
    
    def __init__(self, name):
        self.station_name = name
        self.adjacent_stations = []
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
    
    stations = create_subway_graph("./algorithm/data_structure/stations.txt")  # stations.txt 파일로 그래프를 만든다
    ## print adjacent list of station in stations
    for station in sorted(stations.keys()):
        print(stations[station])
