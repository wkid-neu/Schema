from django.db import models


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



class EntityTab(models.Model):
    entity_name = models.CharField(primary_key=True, max_length=255)
    name_zh = models.CharField(max_length=255)
    super_name = models.CharField(max_length=255)
    entity_url = models.CharField(max_length=255)
    description = models.TextField()
    self_properties = models.TextField(blank=True, null=True)
    all_properties = models.TextField()

    class Meta:
        managed = False
        db_table = 'entity_tab'


class PropertyTab(models.Model):
    property_name = models.CharField(primary_key=True, max_length=255)
    name_zh = models.CharField(max_length=255)
    property_url = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'property_tab'


class UserinfoTab(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=128)
    password = models.CharField(max_length=256)
    email = models.CharField(unique=True, max_length=254)
    sex = models.CharField(max_length=32)
    c_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'userinfo_tab'


class Neo4JEntitiesTab(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    neo4j_id_set = models.TextField()
    neo4j_entity_set = models.TextField()

    class Meta:
        managed = False
        db_table = 'neo4j_entities_tab'
