# Django Serializers
## What is a Serializer?
A serializer is a class that provides a way to convert data into a format that can be easily stored or transmitted. It does so by translating the data into a format that is easy to read and understand by other systems. In Django, serializers are used to convert querysets or model instances into native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.

## Why use Serializers?
We use serializers to convert complex data such as querysets and model instances to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.

## Type of Serializers
There are two types of serializers in Django REST Framework: ModelSerializer and Serializer. ModelSerializer is a shortcut to create serializer classes for Django models. It will automatically generate a set of fields for you, based on the model.

### ModelSerializer
ModelSerializer is a shortcut to create serializer classes for Django models. It will automatically generate a set of fields for you, based on the model.

```python
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'account_name', 'users', 'created'] 

        #fields = '__all__' #all fielfs of the model
        #exclude = ['created'] #exclude fields of the model
```

### Serializer
The Serializer class is the one that gives you the most control, but requires the most amount of work. You have to define all the fields yourself. It is useful if you want to completely customize the resulting response, or if you want to support non-model data structures.

```python
from rest_framework import serializers

class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    account_name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
```

## Serializing and deserializing data
### Serializing objects
```python
serializer = AccountSerializer(account)
serializer.data
# {'id': 1, 'account_name': 'My Account', 'users': [1, 2], 'created': '2019-01-01T00:00:00Z'}
```

### Deserializing objects
```python
serializer = AccountSerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data
# OrderedDict([('account_name', 'My Account'), ('users', [1, 2])])
serializer.save()
# <Account: Account object (1)>
```

## Validation
### Validation on fields
```python
class AccountSerializer(serializers.Serializer):
    account_name = serializers.CharField(max_length=100)
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    def validate_account_name(self, value):
        """
        Check that the blog post is about Django.
        """
        if 'django' not in value.lower():
            raise serializers.ValidationError("Blog post is not about Django")
        return value
```

### Validation on Serializer
```python
class AccountSerializer(serializers.Serializer):
    account_name = serializers.CharField(max_length=100)
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['account_name'] != 'My Account':
            raise serializers.ValidationError("Account name is not valid")
        return data
```

##  Handling related models and nested serializers
### Nested relationships
```python
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class AccountSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ['id', 'account_name', 'users', 'created']
```

### Writable nested serializers
```python

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class AccountSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = Account
        fields = ['id', 'account_name', 'users', 'created']

    def create(self, validated_data):
        users_data = validated_data.pop('users')
        account = Account.objects.create(**validated_data)
        for user_data in users_data:
            User.objects.create(account=account, **user_data)
        return account
```

## Hyperlinked relationships

### HyperlinkedModelSerializer
```python
class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['url', 'account_name', 'users', 'created']
```

### HyperlinkedRelatedField
```python
class AccountSerializer(serializers.ModelSerializer):
    users = serializers.HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)

    class Meta:
        model = Account
        fields = ['id', 'account_name', 'users', 'created']
```


## Relationships and hyperlinked APIs
### HyperlinkedIdentityField
```python
class AccountSerializer(serializers.ModelSerializer):
    users = serializers.HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)
    account_url = serializers.HyperlinkedIdentityField(view_name='account-detail')

    class Meta:
        model = Account
        fields = ['id', 'account_name', 'users', 'created', 'account_url']
```
