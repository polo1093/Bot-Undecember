import time


class Timer():  
    """_summary_
        time_wait in sec
    Returns:
        bool: Tue if timer is full
    """
    def __init__(self,time_wait):
        self.start_time = time.perf_counter()
        self.time_wait = time_wait
    
    def is_expire(self):
        return time.perf_counter()-self.start_time >= self.time_wait    
    
    def is_running(self):
        return time.perf_counter()-self.start_time < self.time_wait



