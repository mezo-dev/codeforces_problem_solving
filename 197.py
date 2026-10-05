


class DeadLineJob:

    def __init__(self):
        self.jobs = {
            "job-1": (5, 3), # profit, deadline
            "job-2": (15, 2),
            "job-3": (10, 1), 
            "job-4": (20, 2), 
            "job-5": (1, 2), 
        }

    def get_hightest_profit(self):
        sorted_jobs = []
        for pt, dl in self.jobs.items():
            
            while dl[0] > dl[1]:
                sorted_jobs.append(self.jobs.get(pt))
        

        print(sorted_jobs)



obj = DeadLineJob()
obj.get_hightest_profit()