speed_of_light = 300000 #km/s
latency = .007
latency_distance = latency * speed_of_light
cost = 100. # US dollars
size = 1000000 * 1000000
cost_per_bit = cost / (size * 8)

print latency_distance
print cost_per_bit * 1000000000