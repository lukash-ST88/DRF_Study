from rest_framework import permissions

"""пользовательские классы доступа"""
class IsAdminOrReadOnlyCust(permissions.BasePermission):
    def has_permission(self, request, view): # ограничение доступа на урвоне всего запроса
        if request.method in permissions.SAFE_METHODS: # если запрос безопасный т.е. GET HEAD OPTION
            return True #разрешаем доступ всем пользователям
        return bool(request.user and request.user.is_staff) #иначе только администратору

class IsOwnerOrReadOnlyCust(permissions.BasePermission):
    def has_object_permission(self, request, view, obj): # ограничение доступа на урвоне объекта(записи)
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user  # если пользователь из базы данных(создавший запись) равен пользователю пришедшему с запросом тогда True

"""ограничение списка ip адрессов занесенных в список заблокированных"""
# class BlocklistPermission(permissions.BasePermission):
#     """
#     Global permission check for blocked IPs.
#     """
#
#     def has_permission(self, request, view):
#         ip_addr = request.META['REMOTE_ADDR']
#         blocked = Blocklist.objects.filter(ip_addr=ip_addr).exists()
#         return not blocked