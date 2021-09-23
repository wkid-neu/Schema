from django.db import models


# Create your models here.


class UserinfoTab(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=128)
    password = models.CharField(max_length=256)
    email = models.CharField(unique=True, max_length=256)
    sex = models.CharField(max_length=32)
    role = models.CharField(max_length=32)
    c_time = models.DateTimeField()
    session = models.CharField(max_length=256, blank=True, null=True)
    login_ip = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userinfo_tab'


class LogininfoTab(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128)
    login_ip = models.CharField(max_length=32)
    login_time = models.CharField(max_length=128)
    status = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'logininfo_tab'




class CreateinfoTab(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    entity_name = models.CharField(max_length=255)
    customize = models.CharField(max_length=1)
    extra_properties = models.TextField(blank=True, null=True)
    fill_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'createinfo_tab'


class Neo4JEntitiesTab(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    neo4j_id_set = models.TextField()
    neo4j_entity_set = models.TextField()

    class Meta:
        managed = False
        db_table = 'neo4j_entities_tab'
