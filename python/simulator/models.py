from django.db import models

class InterviewDocument(models.Model):
    language = models.CharField(max_length=10)  # 用于存储面试时的语言选择
    cv = models.FileField(upload_to='cvs/')  # 存储用户简历
    job_description = models.FileField(upload_to='job_descriptions/')  # 存储招聘启事

    def __str__(self):
        return f"Interview Document in {self.language}"