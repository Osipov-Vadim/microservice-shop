from rest_framework import serializers
from microservices_api import dto
import json


def parse_raw_data(data):
    return json.loads(data.decode('utf-8'))


def get_raw_data(data):
    return json.dumps(data)


class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    amount = serializers.IntegerField()
    price = serializers.FloatField()

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.price = validated_data.get('price', instance.price)
        return instance

    def create(self, validated_data):
        return dto.Item(**validated_data)


class CItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    amount = serializers.IntegerField()
    price = serializers.FloatField()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.price = validated_data.get('price', instance.price)
        return instance

    def create(self, validated_data):
        return dto.CItem(**validated_data)


class ItemAdditionParametersSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    amount = serializers.IntegerField()
    username = serializers.CharField(max_length=100)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.username = validated_data.get('username', instance.username)
        return instance

    def create(self, validated_data):
        return dto.ItemAdditionParameters(**validated_data)


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    status = serializers.ChoiceField(choices=dto.OrderStatus.list())
    username = serializers.CharField(max_length=100)
    totalCost = serializers.FloatField()
    totalAmount = serializers.FloatField()

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.status = validated_data.get('status', instance.status)
        instance.username = validated_data.get('username', instance.username)
        instance.totalCost = validated_data.get('totalCost', instance.totalCost)
        instance.totalAmount = validated_data.get('totalAmount', instance.totalAmount)
        return instance

    def create(self, validated_data):
        return dto.Order(**validated_data)


class OrderIdSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        return instance

    def create(self, validated_data):
        return dto.OrderId(**validated_data)


class OrderStatusSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    status = serializers.ChoiceField(choices=dto.OrderStatus.list())

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        return instance

    def create(self, validated_data):
        return dto.OrderId(**validated_data)


class UserDetailsSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    cardAuthorizationInfo = serializers.ChoiceField(choices=dto.CardAuthorizationInfo.list())

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.cardAuthorizationInfo = validated_data.get('cardAuthorizationInfo', instance.cardAuthorizationInfo)
        return instance

    def create(self, validated_data):
        return dto.UserDetails(**validated_data)

    def check_and_create(self, data):
        json_dict = json.loads(data)
        return self.create(validated_data=json_dict)
