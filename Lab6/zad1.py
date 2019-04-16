import random

T = []
V = []

def create(val, ind):
    global V
    V.append(
        {
            'value' : val,
            'id' : ind,
            'right' : None,
            'left' : None
        }
    )

def add(val, ind):
    global T
    create(val, ind)
    for i in range(0, len(T)):
        try:
            rule = val < T[i]['value'] and val > T[i-1]['value']
        except IndexError:
            rule = True
        if rule:
            if T[i]['left'] == None:
                T[i]['left'] = ind
            elif T[i]['right'] != None and T[i]: #Tu dokoncz
                pass

# def add_right(prev, val, ind):
#     global V
#     i=0
#     while 1:
#         try:
#             rule = lista[i]['id'] == prev
#         except IndexError:
#             print('Vertex not found')
#             return
#         if rule:
#             break
#         else:
#             i += 1
#     vertex = {
#         'value' : val,
#         'id' : ind,
#         'right' : None,
#         'left' : None
#     }
#     V.append(vertex)
#     lista[i]['right'] = vertex['id']

# def add_left(prev, val, ind):
#     global V
#     i=0
#     while 1:
#         try:
#             rule = lista[i]['id'] == prev
#         except IndexError:
#             print('Vertex not found')
#             return
#         if rule:
#             break
#         else:
#             i += 1
#     vertex = {
#         'value' : val,
#         'id' : ind,
#         'right' : None,
#         'left' : None
#     }
#     V.append(vertex)
#     lista[i]['left'] = vertex['id']

# def search_v(val):
#     for i in V:
#         if i[value] == val:
#             return i
#     print('Vertex not found')
#     return None



