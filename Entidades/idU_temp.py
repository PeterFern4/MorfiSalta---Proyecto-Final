import json
class IdUsuario:
    def __init__(self, id):
        self.id = id
        

    def __str__(self):
        return f'''DNI: {self.id}'''

    def a_json(self):
        return {'DNI': self.id}
    
    @classmethod   
    def from_json(cls, data):
        id = data['DNI']
        return IdUsuario(id)
    