import math

# This program finds the closest point to a given origin using either the 2D distance formula (Cartesian) or Haversine formula (GPS coordinates)

def distance(point1, point2, mode):
    
    # Distance calculation based on mode
    if mode == "cartesian":
        x1, y1 = point1
        x2, y2 = point2

        # 2D distance formula
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    elif mode == "gps":
        lat1, lon1 = point1
        lat2, lon2 = point2
        
        # Convert degrees to radians
        lat1, lon1 = math.radians(lat1), math.radians(lon1)
        lat2, lon2 = math.radians(lat2), math.radians(lon2)
        
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        # Haversine formula
        a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        return 6371 * c  # Distance in km


# Choose mode
print("Choose distance mode (cartesian/gps):")
mode = input().strip().lower()

# Validate mode
if mode not in ["cartesian", "gps"]:
    print("Invalid mode. Please choose 'cartesian' or 'gps'.")
    exit()

# Dynamic labels for cleaner code
label = "(x, y)" if mode == "cartesian" else "(latitude, longitude)"
unit = "" if mode == "cartesian" else " km"

# Input origin
print(f"Enter your origin point {label}:")
origin = tuple(map(float, input().split()))

# Input number of points
print("Enter the number of points to compare:")
num_points = int(input())
points = []

# Input each point
for i in range(num_points):
    print(f"Enter point {i + 1} {label}:")
    point = tuple(map(float, input().split()))
    points.append(point)

# Print distances
print(f"\nDistances from {origin} to each point:")
for i, point in enumerate(points, start=1):
    dist = distance(origin, point, mode)
    print(f"Distance to point {i}: {dist:.2f}{unit}")

# Find closest point
min_point = min(points, key=lambda p: distance(origin, p, mode))
min_dist = distance(origin, min_point, mode)

# Return closest point and distance with method used
print(f"\nClosest point to {origin} is {min_point} with distance {min_dist:.2f}{unit} using {mode} mode.")