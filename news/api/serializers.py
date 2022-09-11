from rest_framework import serializers
from news.models import Article

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title =  serializers.CharField()
    description = serializers.CharField()
    text = serializers.CharField()
    city= serializers.CharField()
    publication_date = serializers.DateField()
    status= serializers.BooleanField()
    created_date = serializers.DateTimeField(read_only=True)
    update_date = serializers.DateTimeField(read_only=True)


    def create(self, validated_data):
        print(validated_data)
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author' , instance.author)
        instance.title = validated_data.get('title' , instance.title)
        instance.description = validated_data.get('description' , instance.description)
        instance.text = validated_data.get('text' , instance.text)
        instance.city = validated_data.get( 'city' , instance.city)
        instance.publication_date = validated_data.get('publication_date' , instance.publication_date)
        instance.status = validated_data.get( 'status' , instance.status) 
        instance.save()    


    def validate(self, data):
        print(data)
        if data['title'] == data['description']: 
            raise serializers.ValidationError('baslık ve açıklama aynı olamaz')
        return data    


    def validate_title(self, value):
        if len(value) >20:
            raise  serializers.ValidationError('BASLIK ALANI 20 KARATERİ GECEMEZ')   