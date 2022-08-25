from books.models import Books
import graphene
from graphene_django import DjangoObjectType

class BookType(DjangoObjectType):
    class Meta:
        model = Books
        fields = ("id", "title", "excerpt")


class Query(graphene.ObjectType):
    books = graphene.List(BookType)

    def resolve_books(root, info, **kwargs):
        # Querying a list
        return Books.objects.all()

schema = graphene.Schema(query=Query)
