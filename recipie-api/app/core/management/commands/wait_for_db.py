"""django command for database to be avaliable than run the app"""
from psycopg2 import OperationalError as pyscopgError
from django.db.utils import OperationalError;
import time
from django.core.management import BaseCommand;

class Command(BaseCommand):
    """django class to wait for the database"""
    
    def handle(self, *args, **options):
       self.stdout.write("Wating for database to connect.....")
       db_up = False     
       while db_up is False:
           try:
               self.check(databases=["default"])
               db_up= True
           except(pyscopgError, OperationalError):
               self.stdout.write("Database not avaliable yet")
               time.sleep(1)       
       self.stdout.write(self.style.SUCCESS("Database Avaliable"))
