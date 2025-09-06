# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
# Round up to one decimal point
def calculate_height(h0, t):
    # TODO: Implement this function
    def calculate_height(h0, t):
    g = 9.8  
    height = h0 - 0.5 * g * (t ** 2)
    return round(height, 1)
    initial_height = float(input("Enter initial height: "))
    time = float(input("Enter time: "))
    result = calculate_height(initial_height, time)
    print(f"Height of the ball at time {time} second(s) = {result} meters"

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # TODO: Implement this function
      distance = speed * time
      return round(distance, 1)

      speed = 20  # meters per second
      time = float(input("Enter time for car (in seconds): "))
      result = calculate_car_distance(speed, time)
      print(f"The car will travel {result} meters in {time} second(s).")


