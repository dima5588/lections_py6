# CRUD - C: create, R: read(listing, detail), U: update, D: delete
# from .serch import search_object

# class CreateMixin:
#     def _get_or_set_objects(self):
#         try:
#             self.id
#             self.objects
#         except (NameError, AttributeError):
#             self.objects = []
#             self.id = 0 

#     def __init__(self) -> None:
#         self._get_or_set_objects()

#     def post(self, **kwargs):
#         self.id += 1
#         obj = dict(id=self.id, **kwargs)
#         print(obj, '!!!')

# obj = CreateMixin()
# obj.post(title='Redmi Note 12', description ='The best phone for own price', qty=10, price=250)

# class ReadMixin:
#     def list(self):
#         res = [{'id': obj['id'], 'title': obj['title']} for obj in self.objects]
#         return {'status': '200 OK', 'msg': res}

#     def detail(self, id, **kwargs):
#         objects_id = [x['id'] for x in self.objects] 
#         left = 0
#         right = len(objects_id) - 1
#         mid = len(objects_id) // 2

#         while objects_id[mid] != id and left <= right:
#             if id < objects_id[mid]:
#                 right = mid - 1
#             else :
#                 left = mid + 1
#             mid = (left + right) // 2 
        
#         if left > right:
#             return {'status': '404 Not Found'}
#         return {'status': '200 OK', 'msg': self.objects[mid]}
    
# class UpdateMixin:
#     def patch(self, id, **kwargs)
#         def list(self):
#         res = [{'id': obj['id'], 'title': obj['title']} for obj in self.objects]
#         return {'status': '200 OK', 'msg': res}

#     def detail(self, id, **kwargs):
#         objects_id = [x['id'] for x in self.objects] 
#         left = 0
#         right = len(objects_id) - 1
#         mid = len(objects_id) // 2

#         while objects_id[mid] != id and left <= right:
#             if id < objects_id[mid]:
#                 right = mid - 1
#             else :
#                 left = mid + 1
#             mid = (left + right) // 2 
        
#         if left > right:
#             return {'status': '404 Not Found'}
#         return {'status': '200 OK', 'msg': self.objects[mid]}
    
# class DeleteMixin:
#     @search_object
#     def delete(self, id, **kwargs):
            