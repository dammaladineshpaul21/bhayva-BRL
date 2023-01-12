from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Assest(models.Model):
    id = models.IntegerField(db_column='ID')
    asset_id = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=800)
    file_type = models.CharField(max_length=45)
    file_size = models.CharField(max_length=45)
    language = models.CharField(max_length=45)
    approver = models.CharField(max_length=45)
    approved_date = models.DateTimeField(auto_now=True)
    reviewer = models.CharField(max_length=45)
    reviewer_date = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=45)
    updated_by = models.CharField(max_length=45)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField()
    version = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    objects = models.Manager()