#!/usr/bin/env python3
import re

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self,job=APPROVED_JOBS[0], name='Guido',):
        self.name = name
        self.job = job

    def get_name(self):
        print('Getting the name')       
        return self._name
        
    def set_name(self, name):
        # print(f'Setting the name equal to {name}')
        if(type(name) != str) or (len(name) > 25) or (len(name) < 1) or (not re.search('[a-zA-Z]',name)):
            print("Name must be string between 1 and 25 characters.")        
        elif(0 < len(name) < 25):
            self._name = name.title()
            
    def get_job(self):
        print('Getting the job')       
        return self._job

    def set_job(self, job):
        if(job not in APPROVED_JOBS):  
            print("Job must be in list of approved jobs.")
        else:
            self._job = job
            
    name = property(get_name, set_name)
    job = property(get_job, set_job)
    
