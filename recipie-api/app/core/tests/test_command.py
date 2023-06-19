"""test custom django commands"""

# this will mock the behavoir of the database which means changes the behavoirs of the database
from unittest.mock import patch;

# this is the adapter but we are getting the operationalError which is an error we might get from the database before we connect
from psycopg2 import OperationalError as Psycop2Error;
# to simulate or call the command by the name 
from django.core.management import call_command;

# right here we are saying at any stage if there is an error please send it to me.
from django.db.utils import OperationalError;

# here like we learned we are creating a simple database test which doesn't require a database connection
from django.test import SimpleTestCase;



# first we going to get the from folder which is core than down to command folder than wait_for_db file which has the class Command than there is a check method which checks if the database connected or no 
# command check is provided by the BaseCommand in wait_for_db file to check for the connection
# we will be mocking tehs check method 
# it will simulate thorught an expetion or getting the value 
@patch('core.management.commands.wait_for_db.Command.check')


class CommandTest(SimpleTestCase):
    """test commands we going to do aganist our code"""


    # so the patched_check argument will get the error or the return value from the wait_for_db.py as a value
    # which can be a error or a value 
    def waiting_for_database_to_be_ready(self, patched_check):
        """testing waiting for database to ready"""
        
        # if it works return the value 
        patched_check.return_value = True
        
        # job for the call_command is to execute the code inside the wait_for_db.py file 
        # also this checks if the command is called correctly 
        call_command('wait_for_db')
        
        # here we are making sure that the database is called correctly from the check object
        # default is the one inside the settings.py which has it as a default
        patched_check.assert_called_once_with(database=["default"])
        
        # here we going to delay the application from starting until the database start 
     
     
    # we over writting with mock operation (patch) to make it doesn't sleep.
    @patch("time.sleep")
    
    # here we test the delay operation to make sure everything runs smooth
    def test_wait_for_dataBase_delay(self, patch_sleep, patch_checked):
        
        # side_effect a class that raises the exception
        # so the first error [Psycop2Error] is when there is no connection been accepted to the database 
        # so the second one is haven't setup a the database connection right [Psycop2Error]
        # it return true if return the 6 times 
        patch_checked.side_effect = [Psycop2Error] * 2 \
                [OperationalError] * 3 + [True]
                
        call_command('wait_for_db')
        
        # here we count how many times the patch_checked have been run by the call_count
        self.assertEqual(patch_checked.call_count, 6)
        
        # we said it called database with to call it multiple times because we using side_effect 6 times 
        #   if we need it once that it will be called_once_with
        patch_checked.assert_called_with(database=["default"])