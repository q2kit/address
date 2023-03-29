from django.db import models

# Create your models here.


class Province(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id) + ' - ' + self.name
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class District(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return str(self.id) + ' - ' + self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class Ward(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='wards')

    def __str__(self):
        return str(self.id) + ' - ' + self.name
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }