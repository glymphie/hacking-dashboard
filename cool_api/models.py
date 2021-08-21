from django.db import models

# Create your models here.
class FtpLogin(models.Model):

    date = models.DateTimeField(verbose_name="Date", unique=True, null=True) # Eg. 2015-10-09 23:55:59.342380
    # username = models.CharField(verbose_name="Username", max_length=120, null=True)
    # password: str
    ip = models.GenericIPAddressField(verbose_name="IP") # Eg. 0.0.0.0
    status = models.CharField(verbose_name="Status", max_length=10, null=True) # FAIL / OK

    def __str__(self):
        return f"[{self.date}] {self.ip} : {self.status} "

    @classmethod
    def get_all(cls):
        return cls.objects.all()


class Endlessh(models.Model):
    date = models.DateTimeField(verbose_name="Date", unique=True, null=True) # Eg. 2015-10-09 23:55:59.342380
    ip = models.GenericIPAddressField(verbose_name="IP") # Eg. 0.0.0.0
    time_wasted = models.FloatField(verbose_name='Time_Wasted', null=True) 
    bytes_sent = models.IntegerField(verbose_name='Bytes_Sent', null=True)

    def __str__(self):
        return f"[{self.date}] {self.ip} - Time wasted: {self.time_wasted}, Bytes sent: {self.bytes_sent}"

    @classmethod
    def get_all(cls):
        return cls.objects.all()
