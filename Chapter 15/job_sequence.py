def job_scheduling(seq, num_jobs):
    """Schedule jobs in sequence, based on number of jobs to perform"""

    # Sort jobs in descending order of profit
    seq.sort(key=lambda x: x[-1], reverse=True)

    # Max amount of time allowed
    max_deadline = [False] * num_jobs

    # Sequence of jobs
    job = ['-1'] * num_jobs

    for i in range(len(seq)):  # Iterate through all given jobs
        for j in range(min(num_jobs - 1, seq[i][1] - 1), -1, -1):  # Find a free slot for this job, starting at end of
            # 'job' list
            if max_deadline[j] is False:
                max_deadline[j] = True
                job[j] = seq[i][0]
                break

    return job


if __name__ == "__main__":
    # Job, deadline, profit
    arr = [['a', 2, 100],
           ['b', 1, 19],
           ['c', 2, 27],
           ['d', 1, 25],
           ['e', 3, 15]]

    print(f"For the following job matrix:")
    print(f"Job\t\tDeadline\tProfit")
    for item in arr:
        print(f"{item[0]}\t\t{item[1]}\t\t{item[2]}")

    print("\nThe following sequence of jobs that yield maximum profit:")
    print(job_scheduling(arr, 3))
