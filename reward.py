
def reward_function(params):
    '''
    Example of penalize steering, which helps mitigate zig-zag behaviors. 
	Customized. Logic added to keep all wheels on road as well as more steering encouragement.
    '''

    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    abs_steering = abs(params['steering_angle']) # Only need the absolute steering angle
    all_wheels_on_track = params['all_wheels_on_track']
    is_offtrack = params['is_offtrack']

    if is_offtrack:
        return float(1e-3)

    reward = 0
    if all_wheels_on_track:
        reward += 25

    # Calculate 3 marks that are farther and father away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward += 5.0
    elif distance_from_center <= marker_2:
        reward += 2.5
    elif distance_from_center <= marker_3:
        reward += 1
    else:
        reward += -10.0  # likely crashed/ close to off track

    # Steering penality threshold, change the number based on your action space setting adjusted    
    # Penalize reward if the car is steering too much
    if abs_steering > 12.5:
        reward *= 0.8
    elif abs_steering > 22:
        reward *= 0.6

    return float(reward)
    
