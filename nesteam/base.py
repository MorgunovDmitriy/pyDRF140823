#
#
#
#
# import os
# import sys
#
# from pathlib import Path
# from datetime import timedelta
#
# from dotenv import load_dotenv
#
# REST_FRAMEWORK = {
#     "DEFAULT_PERMISSION_CLASSES": [
#         "rest_framework.permissions.AllowAny",
#     ],
#     "DEFAULT_AUTHENTICATION_CLASSES": (
#         "rest_framework_simplejwt.authentication.JWTAuthentication",
#         'rest_framework.authentication.SessionAuthentication',
#     ),
#     "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
#     "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
#     "PAGE_SIZE": 10,
#     "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
# }