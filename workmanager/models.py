from django.db import models

# Create your models here.

TaskStatuses = {
    'New': 'New',
    'Ready': 'Ready',
    'InProgress': 'In Progress',
    'Done': 'Done'
}


class IDObject(models.Model):
    id = models.AutoField(primary_key=True, default=0)
    pass

    class Meta:
        abstract = True


class NamedObject(IDObject):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Team(NamedObject):
    pass


class Task(NamedObject):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    effort = models.IntegerField(default=0)
    priority = models.IntegerField(default=-1)
    status = models.CharField(
        max_length=10,
        choices=(
            tuple((x, y) for (x, y) in TaskStatuses.items())
        )
    )

    def __str__(self):
        return self.name
