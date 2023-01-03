from email.policy import default
from statistics import mode
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=100)
    contributor = models.CharField(max_length=100)
   
    status = models.TextField()
    
    tasks_subtasks =  models.TextField()

  
    
    
    def get_all_tasks(self):
        tasks_subtasks_inTab = []
        task_subtask = ""
        i = 0
        for letter in self.tasks_subtasks:
            if letter == ';':
                 tasks_subtasks_inTab += [task_subtask]
                 task_subtask = ""
                 i+=1
            else:
                task_subtask+= letter
        tasks_subtasks_inTab +=[task_subtask]
        
        return tasks_subtasks_inTab    
    
    class Meta:
        ordering = ['contributor']
        
        
    
    def get_all_contributor(self):
        contributor_inTab = []
        contributors = ""
        i = 0
        for letter in self.contributor:
            if letter == ';':
                 contributor_inTab += [contributors]
                 contributors = ""
                 i+=1
            else:
                contributors+= letter
        contributor_inTab +=[contributors]
        
        return contributor_inTab      

        
    def get_all_status(self):
        status_inTab = []
        status = ""
        i = 0
        for letter in self.status:
            if letter == ';':
                 status_inTab += [status]
                 status = ""
                 i+=1
            else:
                status+= letter
        status_inTab +=[status]
        
        return status_inTab      
    
    
    
     
      
    
    def __str__(self):
        return self.title
     
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk": self.pk})        
    
class Task(models.Model):
    name = models.CharField(max_length=128)
    users = models.ManyToManyField(User, related_name='tasks')
        