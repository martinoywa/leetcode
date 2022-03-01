class UndergroundSystem:

    def __init__(self):
        # maps for times and stations
        self.idtimes = {}
        self.station = {}
        self.startStopStations = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # insert check in time
        self.idtimes[id] = [t]
        # insert station name
        self.station[id] = [stationName]
        
        # print("CheckIn", self.idtimes, self.station)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # append check out time
        self.idtimes[id].append(t)
        # append station name
        self.station[id].append(stationName)
        
        # print("CheckOut", self.idtimes, self.station)
        
                
        difference = self.idtimes[id][1] - self.idtimes[id][0] 
        
        try:
            if self.startStopStations[tuple(self.station[id])]:
                self.startStopStations[tuple(self.station[id])].append(difference)
        except:
            self.startStopStations[tuple(self.station[id])] = [difference]
            
            
        # remove id from maps
        self.idtimes.pop(id)
        self.station.pop(id)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.startStopStations[(startStation, endStation)]) / len(self.startStopStations[(startStation, endStation)])
        # print("AVG", self.startStopStations)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
