import sys
import signal as sg 
import random

class task_handler:

    """
    taskset: Task details. 
    perc_overrun   : Amount of overrun to be introduced per process. 
    hi_overrun_perc: Percentage of hi tasks exibiting budget overrun. 
    crit_time      : Amount to which system to remain in budget overrun. 
    """
    def __init__(self, taskset, perc_overrun=0.4,
            hi_overrun_perc=0.6, crit_time=40 ):
        self.taskset = taskset
        self.high_pids = {} # Store the high crit task pids.
        self.perc_overrun = perc_overrun # Percentage overrun in high crit tasks.
        self.hi_overr = hi_overrun_perc # Percentange of high crit task exibiting overrun.

    def raise_signal(pid, signame):
        """Raise a signal to given pid."""
        pass

    def raise_budget_overrun(pid, signame):
        """Cause a budget overrun in the given pid."""
        pass 

    def raise_system_criticality(newval):
        """Raise the overall system criticality to the new value."""
        pass 

    def task_launch(params):
        """Launch a rtspin instance with given parameters."""
       pass


