class StationNode:
    """Simple class representing subway station"""
    
    def __init__(self, name):
        self.name = name
        return
    
if __name__ == '__main__':
    ## Init instance for subway station
    station_0 = StationNode('교대역')
    station_1 = StationNode('사당역')
    station_2 = StationNode('종로3가역')
    station_3 = StationNode('서울역')
    
    ## Save StationNodes to python list
    stations = [station_0, station_1, station_2, station_3]
    
    ## Save StationNodes to python dict
    stations = {
        '교대역': station_0,
        '사당역': station_1,
        '종로3가역': station_2,
        '서울역': station_3
    }