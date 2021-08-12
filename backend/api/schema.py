import graphene
from graphene_django import DjangoObjectType
from .models import Restaurant, Item


class RestaurantType(DjangoObjectType):
    class Meta:
        model = Restaurant
        fields = ("id", "name", "address", "phone_number")


class ItemType(DjangoObjectType):
    class Meta:
        model = Item
        fields = ("name", "description", "price", "section", "restaurant")

class Query(graphene.ObjectType):
    all_restaurants = graphene.List(RestaurantType)
    def resolve_all_restaurants(root, info):
        return Restaurant.objects.all()

    one_restaurant = graphene.Field(RestaurantType, id=graphene.Int())
    def resolve_one_restaurant(root, info, id):
        return Restaurant.objects.get(pk=id)

    all_items = graphene.List(ItemType)
    def resolve_all_items(root, info):
        return Item.objects.all()

    one_Item = graphene.Field(ItemType, id=graphene.Int())
    def resolve_one_item(root, info, id):
        return Item.objects.filter(pk=id)
    

class RestaurantMutation(graphene.Mutation):

    class Arguments:
        name = graphene.String(required=False)
        address = graphene.String(required=False)
        phone_number = graphene.String(required=False)

    restaurant = graphene.Field(RestaurantType)

    @classmethod
    def mutate(cls, root, info, name, address, phone_number):
        restaurant = Restaurant(name=name, address=address, phone_number=phone_number)
        restaurant.save()
        return RestaurantMutation(restaurant=restaurant)

class Mutation(graphene.ObjectType):
    update_restaurant = RestaurantMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
