from django.db import migrations
from api.user.models import CustomUser #  Import CustomUser class

# Create a new migration
class Migration(migrations.Migration):

    '''Create a new method, which has:
    - apps represents all the apps we have created
    - schema_editor
    

    '''
    def seed_data(apps, schema_editor):
        # We say that we want a user to be created
        user = CustomUser(name="Hitesh", 
            email="hitesh@lco.dev",
            is_staff=True,
            is_superuser=True,
            phone="954433232",
            gender="Male"
        )

        # We define the password, and would do all the hashing of the password itself
        user.set_password("12345")
        user.save()

    ''' It is going to be dependent on some before migrations
    We for example can see the dependencies that are necessary will be inside of the file that is in
    the folder of migrations of the user app.
    '''
    dependencies = [
        
    ]

    # We also have a part of operations, where we want to run the seed method
    operations = [migrations.RunPython(seed_data),]

