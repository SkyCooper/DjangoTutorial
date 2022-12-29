from rest_framework.pagination import (
  PageNumberPagination,
  LimitOffsetPagination,
  CursorPagination
)

class CustomPageNumberPagination(PageNumberPagination):
  page_size = 5
  page_query_param = 'sayfa'
 
class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3
    limit_query_param = 'adet'
    limit_query_description = ('Sayfa basina sonuclar')
    offset_query_param = 'bitis'
 
class CustomCursorPagination(CursorPagination):
    cursor_query_param = 'imlec'
    page_size = 3
    ordering = 'id'