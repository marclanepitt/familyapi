from knox.models import AuthToken


def generate(token_model, user, serializer):
    return token_model.objects.create(user=user)
