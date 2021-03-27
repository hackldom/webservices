from rest_framework import serializers
from .models import NewsStory, Author

class NewsStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsStory
        fields = ('id', 'url', 'headline', 'category', 'region', 'author', 'date', 'details')
        
class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'url', 'name', 'username', 'password')