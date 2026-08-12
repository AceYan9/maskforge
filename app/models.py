from enum import StrEnum

from tortoise import fields, models


class TaskStatus(StrEnum):
    CREATED = "created"
    ANALYZING = "analyzing"
    READY = "ready"


class BaseModel(models.Model):
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(null=True, default=None)

    class Meta:
        abstract = True


class Task(BaseModel):
    user_id = fields.BigIntField(null=True, default=None)
    task_id = fields.CharField(max_length=32, unique=True)
    filename = fields.CharField(max_length=255)
    file_type = fields.CharField(max_length=20)
    file_size = fields.BigIntField()
    source_object = fields.CharField(max_length=500)
    total_rows = fields.BigIntField(null=True, default=None)
    total_columns = fields.IntField(null=True, default=None)
    status = fields.CharField(max_length=32, default=TaskStatus.CREATED)


class MaskRule(BaseModel):
    task_id = fields.CharField(max_length=32, unique=True)
    rules = fields.JSONField()
