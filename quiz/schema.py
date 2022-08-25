import graphene
from graphene_django import DjangoObjectType, DjangoListField
from quiz.models import Question, Quizzes, Answer, Category

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id", "title", "category")

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("id", "quiz", "question_type", "title", "level", "is_active")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("id", "question", "answer_text", "is_right")


class Query(graphene.ObjectType):
    all_quizzes = graphene.Field(QuizzesType, id=graphene.Int())

    all_questions = graphene.Field(QuestionType, id=graphene.Int())

    all_answers = graphene.List(AnswerType, id=graphene.Int())

    def resolve_all_quizzes(root, info, id):
        return Quizzes.objects.get(pk=id)

    def resolve_all_questions(root, info, id):
        return Question.objects.get(pk=id)

    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)


class CreateCategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    # what we are returning
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name):
        category = Category(name=name)
        category.save()
        return CreateCategoryMutation(category=category)


class UpdateCategoryMutation(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        name = graphene.String()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name, id):
        category = Category.objects.get(id=id)
        category.name = name
        category.save()
        return UpdateCategoryMutation(category=category)


class DeleteCategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(id=id)
        category.delete()
        return DeleteCategoryMutation(category=category)


class Mutation(graphene.ObjectType):
    new_category = CreateCategoryMutation.Field()
    update_category = UpdateCategoryMutation.Field()
    delete_category = DeleteCategoryMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)