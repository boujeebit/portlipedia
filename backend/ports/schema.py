from django.db.models import Q
from graphene_django import DjangoObjectType
import graphene
from ports.models import Port

class PortType(DjangoObjectType):
    class Meta:
        model = Port

class Query(graphene.ObjectType):
    ports = graphene.List(PortType)
    port  = graphene.List(PortType, port=graphene.Int())

    search = graphene.List(PortType, search=graphene.String(), first=graphene.Int(), skip=graphene.Int())

    def resolve_ports(self, info):
        return Port.objects.all()

    def resolve_port(self, info,  **kwargs):
        return Port.objects.filter(port=kwargs.get('port'))

    def resolve_search(self, info, first=None, skip=None, **kwargs):
        search = kwargs.get('search')
        try:
            port = int(search)
            results = Port.objects.filter(port=port)
        except ValueError:
            results = Port.objects.filter(Q(name__icontains=search) | Q(description__icontains=search))

        if skip is not None : 
            results = results[skip:]
        if first is not None: 
            results = results[:first]

        print(skip, first)

        return results

schema = graphene.Schema(query=Query)