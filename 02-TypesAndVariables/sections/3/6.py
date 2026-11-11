average_eye_level_height = 1.6

def distance2horizon(height):
    return 3.57 * height // 2

print("Distance to horizon when standing on the beach:", distance2horizon(0 + average_eye_level_height), "km")
print("Distance to horizon when looking from the window:", distance2horizon(20 + average_eye_level_height), "km")

