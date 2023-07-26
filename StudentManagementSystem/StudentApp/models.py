from django.db import models


# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.course_name}"


class City(models.Model):
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city_name}"


class Student(models.Model):
    stud_name = models.CharField(max_length=50)
    stud_phno = models.BigIntegerField()
    stud_email = models.CharField(max_length=50)
    stud_city = models.ForeignKey(City, on_delete=models.CASCADE)
    stud_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    stud_fees = models.IntegerField()

    def __str__(self):
        return f"{self.stud_name}"


class Trainer(models.Model):
    trainer_name = models.CharField(max_length=50)
    trainer_phno = models.BigIntegerField()
    trainer_email = models.CharField(max_length=50)
    trainer_city = models.ForeignKey(City, on_delete=models.CASCADE)
    teaching_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    trainer_salary = models.IntegerField()

    def __str__(self):
        return f"{self.trainer_name}"
