from uuid import uuid4
from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='created_by_%(class)s',
        null=True,
        blank=True
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='updated_by_%(class)s',
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class Program(BaseModel):
    name = models.TextField()

    def __str__(self):
        return self.name


class Earn(BaseModel):
    program = models.ForeignKey(
        Program,
        on_delete=models.CASCADE,
        related_name="program_earns",
    )
    description = models.TextField(blank=True)
    points = models.IntegerField()
    price = models.FloatField(null=True, blank=True, default=0)
    datetime = models.DateTimeField()
    received_datetime = models.DateTimeField(blank=True, null=True, default=None)
    mil_price = models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return "{} - {} - {}".format(self.program.name, self.points, self.description)

    def save(self, *args, **kwargs):
        if self.points:
            self.mil_price = self.price / (self.points / 1000)  
        super().save(*args, **kwargs)
