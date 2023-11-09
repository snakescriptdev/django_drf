# Relationships and Hyperlinked APIs

## Relationships

In Django we use relationships to define how different parts of our application are connected to each other. We can use relationships to define a one-to-one, one-to-many, or many-to-many relationship between different parts of our application.


## hyperlinking our API

We can hyperlink our API by using HyperlinkedModelSerializer instead of ModelSerializer. This will give us hyperlinks to other endpoints instead of primary keys.

## HyperlinkedModelSerializer

HyperlinkedModelSerializer is similar to ModelSerializer except that it uses hyperlinks to represent relationships, rather than primary keys. This is useful for cases where you don't want to include the related data inline, and instead you want to simply provide a link to the associated data.

## HyperlinkedIdentityField

HyperlinkedIdentityField is similar to the ModelSerializer except that it uses hyperlinks to represent relationships, rather than primary keys. This is useful for cases where you don't want to include the related data inline, and instead you want to simply provide a link to the associated data.

```python
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='snippet-detail', read_only=True)
    class Meta:
        model = Snippet
        fields = ['url', 'id', 'title', 'code', 'linenos', 'language', 'style']

```

## HyperlinkedRelatedField

HyperlinkedRelatedField is similar to the ModelSerializer except that it uses hyperlinks to represent relationships, rather than primary keys. This is useful for cases where you don't want to include the related data inline, and instead you want to simply provide a link to the associated data.

```python
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(
        view_name='user-detail', read_only=True)
    class Meta:
        model = Snippet
        fields = ['url', 'id', 'title', 'code', 'linenos', 'language', 'style', 'owner']

```