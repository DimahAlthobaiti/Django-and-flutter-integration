from django.db import models

class Pose(models.Model):
    motor1 = models.IntegerField()
    motor2 = models.IntegerField()
    motor3 = models.IntegerField()
    motor4 = models.IntegerField()

    def __str__(self):
        return f"Pose {self.id}"

class Run(models.Model):
    motor1 = models.IntegerField()
    motor2 = models.IntegerField()
    motor3 = models.IntegerField()
    motor4 = models.IntegerField()
    status = models.IntegerField(default=0)

    def __str__(self):
        return f"Run: M1={self.motor1}, M2={self.motor2}, M3={self.motor3}, M4={self.motor4}, Status={self.status}"