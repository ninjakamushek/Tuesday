from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
import uuid


class Contributor(models.Model):
    name = models.CharField(max_length=20, help_text='Enter your name', unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('contributor-detail', args=[str(self.id)])

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Board(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a board name')
    contributors = models.ManyToManyField(Contributor, help_text='List of contributors')

    def get_absolute_url(self):
        return reverse('board-detail', args=[str(self.id)])

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular task across whole board')
    board = models.ForeignKey('Board', on_delete=models.RESTRICT, null=True)
    description = models.CharField(max_length=1000, help_text='Description of the task')
    deadline = models.DateField(null=True, blank=True)
    PROGRESS_STATUS = (
        ('w', 'in work'),
        ('fn', 'finished'),
        ('fr', 'frozen'),
    )
    status = models.CharField(
        max_length=2,
        choices=PROGRESS_STATUS,
        blank=True,
        default='w',
        help_text='task status',
    )

    class Meta:
        ordering = ['deadline']
        permissions = (())

    def __str__(self):
        return f'{self.id} ({self.board.name})'

