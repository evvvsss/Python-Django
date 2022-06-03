from asgiref.sync import sync_to_async
from django.contrib.auth.models import User, AnonymousUser


class TokenAuthMiddlewareFromPath:
    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        scope['user'] = AnonymousUser()
        try:
            user_id = scope['path'].split('/')[-2]
            scope['user'] = await sync_to_async(lambda: User.objects.get(id=user_id))()
        except Exception:
            ...
        return await self.inner(scope, receive, send)
