import random

# Constants
busy = 1
idle = 0
nevents = 2


# Initialize the simulation
def init(idle, marrvt):
    sim_time = 0.0
    server_status = idle
    num_in_q = 0
    time_last_event = 0.0
    num_custs_delayed = 0
    total_of_delays = 0.0
    area_num_in_q = 0.0
    area_server_status = 0.0
    time_next_event = [0.0, sim_time + random.expovariate(1.0 / marrvt), 1.0e+30]
    return sim_time, num_custs_delayed, total_of_delays, area_num_in_q, area_server_status, time_last_event, time_next_event, server_status, num_in_q


def timing(sim_time, time_next_event):
    min_time_next_event = 1.0e+29
    next_event_type = 0
    for i in range(1, nevents + 1):
        if time_next_event[i] < min_time_next_event:
            min_time_next_event = time_next_event[i]
            next_event_type = i
    if next_event_type == 0:
        print('Event list empty at time', sim_time)
        exit(1)
    sim_time = min_time_next_event
    return sim_time, next_event_type


def arrive(sim_time, time_next_event, server_status, num_in_q, total_of_delays, num_custs_delayed, marrvt, mservt):
    time_next_event[1] = sim_time + random.expovariate(1.0 / marrvt)
    if server_status == busy:
        num_in_q += 1
    else:
        delay = 0.0
        total_of_delays += delay
        num_custs_delayed += 1
        server_status = busy
        time_next_event[2] = sim_time + random.expovariate(1.0 / mservt)
    return time_next_event, server_status, num_in_q, total_of_delays, num_custs_delayed


def depart(sim_time, time_next_event, server_status, num_in_q, total_of_delays, num_custs_delayed, mservt):
    if num_in_q == 0:
        server_status = idle
        time_next_event[2] = 1.0e+30
    else:
        num_in_q -= 1
        delay = sim_time - time_next_event[0]
        total_of_delays += delay
        num_custs_delayed += 1
        time_next_event[2] = sim_time + random.expovariate(1.0 / mservt)
    return time_next_event, server_status, num_in_q, total_of_delays, num_custs_delayed


def report(num_custs_delayed, total_of_delays, area_num_in_q, sim_time, area_server_status):
    print(f'Total number of customers delayed: {num_custs_delayed}')
    print(f'Average delay in queue: {total_of_delays / num_custs_delayed:.3f} minutes')
    print(f'Average number in queue: {area_num_in_q / sim_time:.3f}')
    print(f'Utilization: {area_server_status / sim_time:.3f}')


def update_time_avg_stats(sim_time, time_last_event, num_in_q, server_status, area_num_in_q, area_server_status):
    time_since_last_event = sim_time - time_last_event
    area_num_in_q += num_in_q * time_since_last_event
    area_server_status += server_status * time_since_last_event
    time_last_event = sim_time
    return time_last_event, area_num_in_q, area_server_status


def main():
    # Read input parameters
    marrvt = float(input('Mean interarrival time: '))
    mservt = float(input('Mean service time: '))
    totcus = int(input('Total number of customers: '))

    # Initialize the simulation
    sim_time, num_custs_delayed, total_of_delays, area_num_in_q, area_server_status, time_last_event, time_next_event, server_status, num_in_q = init(
        idle, marrvt)

    # Run the simulation
    while num_custs_delayed < totcus:
        sim_time, next_event_type = timing(sim_time, time_next_event)
        time_last_event, area_num_in_q, area_server_status = update_time_avg_stats(sim_time, time_last_event, num_in_q,
                                                                                   server_status, area_num_in_q,
                                                                                   area_server_status)
        if next_event_type == 1:
            time_next_event, server_status, num_in_q, total_of_delays, num_custs_delayed = arrive(sim_time,
                                                                                                  time_next_event,
                                                                                                  server_status,
                                                                                                  num_in_q,
                                                                                                  total_of_delays,
                                                                                                  num_custs_delayed,
                                                                                                  marrvt, mservt)
        elif next_event_type == 2:
            time_next_event, server_status, num_in_q, total_of_delays, num_custs_delayed = depart(sim_time,
                                                                                                  time_next_event,
                                                                                                  server_status,
                                                                                                  num_in_q,
                                                                                                  total_of_delays,
                                                                                                  num_custs_delayed,
                                                                                                  mservt)

    # Generate report
    report(num_custs_delayed, total_of_delays, area_num_in_q, sim_time, area_server_status)


if __name__ == "__main__":
    main()
