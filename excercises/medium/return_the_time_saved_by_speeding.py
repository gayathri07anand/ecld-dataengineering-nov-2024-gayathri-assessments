def time_saved(speed_limit, avg_speed, distance_travelled):

    time_for_speed_limit = distance_travelled/speed_limit

    time_for_avg_speed = distance_travelled/avg_speed

    time_difference = time_for_speed_limit-time_for_avg_speed

    saved_time = time_difference*60

    return round(saved_time,1)


# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
x,y,z = int(x),int(y),int(z)
difference = time_saved(x,y,z)
print(f"Saved Time : {difference}")
