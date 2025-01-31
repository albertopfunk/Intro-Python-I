# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon(object):
  def __init__(self, lat, lon):
    self.lat=lat
    self.lon=lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
  def __init__(self, lat, lon, name):
    LatLon.__init__(self, lat, lon)
    self.name = name

  def __str__(self):
    return f"{self.name}, {self.lat}, {self.lon}"


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
  def __init__(self, lat, lon, name, difficulty, size):
    Waypoint.__init__(self, lat, lon, name)
    self.difficulty = difficulty
    self.size = size

  def __str__(self):
    return f"{self.name}, {self.lat}, {self.lon}, {self.difficulty}, {self.size}"

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint(45,-45, "LA")
print(waypoint)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache(25,-25, "NY", 150, 5)

# Print it--also make this print more nicely
print(geocache)


# more examples with MRO
class Forcast:
  def __init__(self, forcast):
    self.forcast = forcast

class CurrentLocation(LatLon):
  def __init__(self, lat, lon, time):
    LatLon.__init__(self, lat, lon)
    self.time = time

class CurrentForcast(Forcast, CurrentLocation):
  def __init__(self, forcast, lat, lon, time, planet):
    Forcast.__init__(self, forcast)
    CurrentLocation.__init__(self, lat, lon, time)
    self.planet = planet

currE = CurrentForcast("gloomy", 45, -45, "now", "earth")
print(currE.planet)
