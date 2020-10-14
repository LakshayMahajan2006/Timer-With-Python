# Timer-With-Python

import time
print("Press Enter to start the timer")
while True:
    try:
        input()
        starttime = time.time()
        print("Timer Started.")
        while True:
            print("Time elapsed: ", round(
                time.time()-starttime, 0), 'secs', end='\r')
            time.sleep(1)

    except KeyboardInterrupt:
        print("Bye......")
        endtime = time.time()
        print('Total time: ', round(endtime-starttime, 2))
