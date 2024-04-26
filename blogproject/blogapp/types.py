import strawberry
from typing import List

import strawberry.django
import models

@strawberry.django.type(models.Post)
class PostType:
    id: int
    title: str
    author: str
    message: str