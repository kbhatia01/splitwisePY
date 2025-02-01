import uuid

from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(primary_key=True)

    class Meta:
        abstract = True


class ExpenseType(models.TextChoices):
    Normal = ("NORMAL", "Normal")
    SETTLE_UP_EXPENSE = "SETTLE_UP_EXPENSE", "SETTLE_UP_EXPENSE"


class User(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)


class UserExpenseType(models.TextChoices):
    PAID_EXPENSE = "PAID_EXPENSE", "PAID_EXPENSE"
    OWES_EXPENSE = "OWES_EXPENSE", "OWES_EXPENSE"


class Group(BaseModel):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name="user_groups")
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Expense(BaseModel):
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    expense_type = models.CharField(max_length=20, choices=ExpenseType.choices)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class UserExpense(BaseModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense = models.ForeignKey(Expense, on_delete=models.DO_NOTHING)
    user_expense_type = models.CharField(max_length=20, choices=UserExpenseType.choices)


# class Student(models.Model):
#     name = models.CharField(max_length=255)
#     id = models.UUIDField(primary_key=True)
#
#
# class course(models.Model):
#     title = models.CharField(max_length=255)
#     students = models.ManyToManyField(Student, related_name="student_courses")
#
#
# s1 = Student.objects.create(name="S1")
# s2 = Student.objects.create(name="S2")
# #
# c1 = course.objects.create(title="C1", id=1)
# c2 = course.objects.create(title="C2", id=2)
#
# c1.students.add(s1)
# c1.students.add(s2)
#
# c2.students.add(s1)
# #
# # c1.students.all()
# #
# #
# # s1.student_courses.all()
