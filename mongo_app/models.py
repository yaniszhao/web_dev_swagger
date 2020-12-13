from django.db import models

# Create your models here.

import mongoengine

class DeviceInfo(mongoengine.Document):
    dev_id = mongoengine.SequenceField()
    dev_name = mongoengine.StringField(required=True)
    dev_desc = mongoengine.StringField()
    dev_paras = mongoengine.ListField()


class ParameterInfo(mongoengine.Document):
    para_id = mongoengine.SequenceField(primary_key=True)
    para_name = mongoengine.StringField()
    para_desc = mongoengine.StringField()
