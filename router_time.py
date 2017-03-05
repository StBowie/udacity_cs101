traceroute = 75 #ms
distance = 2 * 2500
c = 300000 #km/s
fibre = .6667 * c #km/s

time_at_router = traceroute - distance / (fibre/1000)
print time_at_router