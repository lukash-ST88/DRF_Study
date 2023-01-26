from rest_framework.pagination import PageNumberPagination


class WomenPaginationAPI(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size_cust' #пользовательский размер страницы
    max_page_size = 4 # макс размер страницы