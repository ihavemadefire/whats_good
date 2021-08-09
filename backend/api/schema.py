import graphene
from graphene_django import DjangoObjectType
from .models import Restaurant, Item


class RestaurantType(DjangoObjectType):
    class Meta:
        model = Restaurant
        fields = ("name", "address", "phone_number")


class ItemType(DjangoObjectType):
    class Meta:
        model = Item
        fields = ("name", "description", "price", "section", "restaurant")

class Query(graphene.ObjectType):
    all_restaurants = graphene.List(RestaurantType)
    def resolve_all_restaurants(root, info):
        return Restaurant.objects.all()

    all_items = graphene.List(ItemType)
    def resolve_all_items(root, info):
        return Item.objects.all()

schema = graphene.Schema(query=Query)
