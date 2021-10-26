from django.db import models
"""
Here pre_save is taken because over save method is before the
default save method like super().save if our defined function
is after the super then we will use post save
"""

# custom model manager and custom query set for filtering our data
# and not to repeat much

class PublishStateOptions(models.TextChoices):
    # CONSTANT = DB_VALUE, USER_DISPLAY_VA
    PUBLISH = 'PU', 'Publish'
    DRAFT = 'DR', 'Draft'
    # UNLISTED = 'UN', 'Unlisted'
    # Private = 'PR', 'Private'
    