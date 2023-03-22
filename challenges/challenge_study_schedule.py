def study_schedule(permanence_period, target_time):
    counter = 0

    for period in permanence_period:
        try:
            if period[0] <= target_time <= period[1]:
                counter += 1
        except TypeError:
            return None

    return counter


print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5)], 3))
