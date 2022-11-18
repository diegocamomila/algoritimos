def study_schedule(permanence_period, target_time):

    counter_study = 0

    for period in permanence_period:
        try:
            if target_time >= period[0] and target_time <= period[1]:
                counter_study += 1
        except (ValueError, TypeError):
            return None

    return counter_study
