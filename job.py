import datetime

class Job():

    """
    A class definition to hold all the information about a job.

        name   : string
            Name of the job.
        start_time : string
               When the job started
              end_time : string
               When the job finished
        status: number
            Status of the job. If it is 0 means success, all othe values means failure

    """
    def __init__(self, name="", start_time=0, end_time=0, status=0):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.status = status

    def get_start_time_obj(self):
        return datetime.datetime.strptime(self.start_time, '%Y-%m-%d.%H:%M:%S')
    def get_end_time_obj(self):
        return datetime.datetime.strptime(self.end_time, '%Y-%m-%d.%H:%M:%S')