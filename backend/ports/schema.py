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

    search = graphene.List(PortType, search=graphene.String())

    def resolve_ports(self, info):
        return Port.objects.all()

    def resolve_port(self, info,  **kwargs):
        return Port.objects.filter(port=kwargs.get('port'))

    def resolve_search(self, info,  **kwargs):
        search = kwargs.get('search')
        try:
            port = int(search)
            return Port.objects.filter(port=port)
        except ValueError:
            return Port.objects.filter(Q(name__icontains=search) | Q(description__icontains=search))

schema = graphene.Schema(query=Query)