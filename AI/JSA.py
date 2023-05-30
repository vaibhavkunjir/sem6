def jobScheduling(jobs):
    n = len(jobs)
    # Sort jobs by decreasing order of their profits
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Create a result array to store the selected jobs
    result = [False] * n
    # Create an array to track the time slots
    timeSlots = [-1] * n

    # Iterate through all the jobs
    for i in range(n):
        # Find the latest available time slot for the current job
        for j in range(min(n, jobs[i][1]) - 1, -1, -1):
            if timeSlots[j] == -1:
                timeSlots[j] = i
                result[i] = True
                break

    # Print the selected jobs
    print("Selected Jobs:")
    for i in range(n):
        if result[i]:
            print("Job", jobs[i][0])

# Example usage:
jobs = [("Job1", 3, 35), ("Job2", 4, 30), ("Job3", 4, 25),
        ("Job4", 2, 20), ("Job5", 3, 15), ("Job6", 1, 12)]
jobScheduling(jobs)
