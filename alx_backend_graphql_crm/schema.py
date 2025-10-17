# alx_backend_graphql_crm/schema.py
import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(description="Returns a friendly greeting")

    def resolve_hello(root, info):
        return "Hello, GraphQL!"

schema = graphene.Schema(query=Query)
