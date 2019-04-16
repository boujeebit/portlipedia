import graphene
import ports.schema

class Query(ports.schema.Query, graphene.ObjectType):
    pass
    
schema = graphene.Schema(query=Query)

# import ports.mutation

# class Mutation(gqlauth.schema.Mutation, records.schema.Mutation, ports.mutation.Mutation, nodes.schema.Mutation, network.schema.Mutation, agents.schema.Mutation, graphene.ObjectType):
#     pass

# schema = graphene.Schema(query=Query, mutation=Mutation)
