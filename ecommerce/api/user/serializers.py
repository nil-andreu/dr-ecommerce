from rest_framework import serializers
# The following will allow to bring the password in the clear text or plaintext format and then hashes it
from django.contrib.auth.hashers import make_password
# And then import some decorators we need
from rest_framework.decorators import authentication_classes, permission_classes

from .models import CustomUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # We now define the methods of create and update as we want the users to be able to be created and update their parameters
    def create(self, validated_data):
        # The property we want to bring in is the password
        password = validated_data.pop('password', None) # Look for the property password, and obtain it's value

        # And we have to create the instance, which is going to interact with the model and will be saving it based on that instance
        # This instance is going to come from the Meta part of the serializer, and to model
        instance = self.Meta.model(**validated_data)
        '''If we check the model, we can see that there is no password field. This is because i do not want this
        password to be visible everywhere. So i only want to extract password from validated data.
        We will also handle the sanitasation of the data in the views part'''

        # In the case this password is not None, we are going to set the password in the instance
        if password is not None:
            instance.set_password(password)
        
        # Save and return the instance
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        # For updating, the instance is already created so it is given
        for attr, value in validated_data.items():
            # In the case it is password
            if attr == "password":
                instance.set_password(value)
            else:
                # We are going to update the other attributes normally
                setattr(instance, attr, value)
        instance.save()
        return instance
    
    class Meta:
        model = CustomUser

        # Now we add the extra parameters that we want to add to be handled by the database
        extra_kwargs = {'password':{'write_only':True},}
        # For example to add the functionality to edit the password. In the case of password,
        # i pass the properties i want for it

        fields = ('name','email','password','phone','gender','is_active','is_staff','is_superuser')
        # The ones of is_staff, is_active of is_superuser are the ones inherited from AbstractUser
        
