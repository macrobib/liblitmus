"""
Read the process description in json files and create rtspin task set.
"""
import sys
import json
import os
import glob
from pprint import pprint

class json_handler:

    """
    path: Path to json file.
    pretty: Pretty print the json output.
    """
    def __init__(self, path='./data', pretty=False):
        self.path = path
        self.high_tasks = []
        self.low_tasks = []
        self.crit = 0
        if pretty:
            # Do a pretty print of json data.
            pprint(self.data)

    def read_taskset(self, file):
        taskset = None
        try:
            with open(file, 'r') as f:
                taskset = json.load(f)
        except (OSError, IOError) as e:
            print("Error opening file: ", e)
        return file
            

    def parse_files(self, file = None):
        """Create the task structure."""
        crit = None
        taskset = []
        if file:
            taskset.append(read_task_set(file))
        else:
            # Parse the default files and read taskset.
            for file in glob.glob('./data/*.json'):
                with open(file, 'r') as f:
                    taskset.append(read_taskset(file))
        # Process task set.
        for task in taskset:
            if task["syscrit"] > self.crit:
                self.crit = taskset["syscrit"]
            if not task["high"]:
                self.high_tasks.append(task["high"])
            if not task["low"]:
                self.low_tasks.append(task["low"])


    def get_system_criticality(self):
        """Retrieve the system criticality requested."""
        return self.crit


    def get_task_set(self):
        """Retrieve the task set processed."""
        return (self.high_tasks, self.low_tasks)


    def high_crit_tasks(self):
        """Get dictionary of all the high criticality tasks."""
        return self.high_tasks


    def low_crit_tasks(self):
        """Get the dictionary of all low crit tasks."""
        return self.low_tasks

