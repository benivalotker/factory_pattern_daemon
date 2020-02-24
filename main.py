#/path/path/
#title           :Title 
#description     :Description.
#update date     :01/01/2020 12:10
#version         :1.0
#changes         :new version changes description.
#python_version  :3.6  
#==============================================================================

import time
import threading
import thread_handler

'''
Daemon Threads - thread shut down when the caller script is done or after all the thread is close. 
    - name   = custom thread name
    - target = function to run
    - args   = function args (as a tuples)
    - daemon = True/Flase
'''
# declare the threads object
thread_obj_1 = threading.Thread(
    name="Custom Thread 1",
    target=thread_handler.thread_handler,
    args=("thread_number_1", ),
    daemon=True
)

thread_obj_2 = threading.Thread(
    name="Custom Thread 2",
    target=thread_handler.thread_handler,
    args=("thread_number_2", ),
    daemon=True
)

# start threads running
thread_obj_1.start()
thread_obj_2.start()


# check if the thread is alive (finish is job or error)
# in this case if one thread is dead the all thread shut down
while(True):
    time.sleep(1)
    if thread_obj_1.is_alive() != None:
        break
    if thread_obj_2.is_alive() != None:
        break
