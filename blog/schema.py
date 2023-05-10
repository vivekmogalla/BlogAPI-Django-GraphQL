import graphene
from graphene_django import DjangoObjectType
from .models import Post, Comment


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields =("id", "title", "description", "publish_date", "author", "comments")


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = ("id", "post", "text", "author_name", "created_at")


class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        publish_date = graphene.Date(required=True)
        author = graphene.String(required=True)

    post =graphene.Field(PostType)

    def mutate(self, info, title, description, publish_date, author):
        post = Post(title=title, description=description,
                    publish_date=publish_date, author=author)
        post.save()
        return CreatePost(post=post)


class UpdatePost(graphene.Mutation):
    class Arguments:
        post_id = graphene.ID(required=True)
        title = graphene.String(required=True)
        description = graphene.String()
        publish_date = graphene.Date()
        author = graphene.String()

    post = graphene.Field(PostType)

    def mutate(self, info, post_id, title=None, description=None, publish_date=None, author=None):
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            raise ValueError(f"Post with id {post_id} does not exist")
        if title:
            post.title = title
        if description:
            post.description = description
        if publish_date:
            post.publish_date = publish_date
        if author:
            post.author = author
        post.save()
        return UpdatePost(post=post)


class CreateComment(graphene.Mutation):
    class Arguments:
        post_id = graphene.ID(required=True)
        text = graphene.String(required=True)
        author_name = graphene.String(required=True)

    comment =graphene.Field(CommentType)

    def mutate(self, info, post_id, text, author_name):
        post = Post.objects.get(pk=post_id)
        comment = Comment(post=post, text=text, author_name=author_name)
        comment.save()
        return CreateComment(comment=comment)


class DeleteComment(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            comment = Comment.objects.get(id=id)
            comment.delete()
            ok = True
        except Comment.DoesNotExist:
            ok = False
        return DeleteComment(ok=ok)


class Mutation(graphene.ObjectType):
    create_post =CreatePost.Field()
    update_post = UpdatePost.Field()
    create_comment = CreateComment.Field()
    delete_comment = DeleteComment.Field()


class Query(graphene.ObjectType):
    all_posts =graphene.List(PostType)
    post_by_id = graphene.Field(PostType, id=graphene.Int(required=True))
    all_comments = graphene.List(CommentType)
    comment_by_id = graphene.Field(CommentType, id=graphene.Int(required=True))

    def resolve_all_posts(self, info):
        return Post.objects.all()

    def resolve_post_by_id(self, info, id):
        return Post.objects.get(id=id)

    def resolve_all_comments(self, info):
        return Comment.objects.all()

    def resolve_comment_by_id(self, info, id):
        return Comment.objects.get(id=id)

# combining the Query and Mutation to define the Schema
schema = graphene.Schema(query=Query, mutation=Mutation)