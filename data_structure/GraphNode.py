from typing import Dict


class StationNode:
    """Simple class representing subway station"""
    
    def __init__(self, name):
        self.station_name = name
        return

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
    stations = create_station_nodes("./algorithm/data_structure/stations.txt")  # stations.txt 파일로 그래프 노드들을 만든다

    # stations에 저장한 역들 이름 출력 (채점을 위해 역 이름 순서대로 출력)
    for station in sorted(stations.keys()):
        print(stations[station].station_name)