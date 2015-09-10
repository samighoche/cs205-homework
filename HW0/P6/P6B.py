import multiprocessing as mp
import time
import matplotlib.pyplot as plt

# Sleep for t seconds
def burnTime(t):
    time.sleep(t)

# Main
if __name__ == '__main__':
    N = 16  # The number of jobs
    P = 4   # The number of processes

    # A thread pool of P processes
    pool = mp.Pool(P)

    # Use a variety of wait times
    ratio = []
    wait_time = [0.000001*i for i in range(1,10)] + [0.00001*i for i in range(1,10)] + [0.0001*i for i in range(1,10)] + [0.001*i for i in range(1,10)] + [0.01*i for i in range(1,10)] + [0.1*i for i in range(1,10)] + [1]

    for t in wait_time:
        # Compute jobs serially and in parallel
        # Use time.time() to compute the elapsed time for each
        serialStart = time.time()
        for i in range(16):
            burnTime(t)
        serialTime = time.time() - serialStart
        
        parallelStart = time.time()
        pool.map(burnTime, [t for i in range(16)])
        parallelTime = time.time() - parallelStart
        # Compute the ratio of these times
        ratio.append(serialTime/parallelTime)

    # Plot the results
    plt.plot(wait_time, ratio, '-ob')
    plt.xscale('log')
    plt.xlabel('Wait Time (sec)')
    plt.ylabel('Serial Time (sec) / Parallel Time (sec)')
    plt.title('Speedup versus function time')
    plt.show()
