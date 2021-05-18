import random

n = None
tree = None
queries = None

print("Алгоритм Тарьяна (Нахождение наименьшего общего предка)")
print("Необходимо записать структура дерева, формат ввода : vertex_from vertex_to)")
print("После структуры дерева в новой строке ввести кол-во запросов")
print("В каждой новой строке ввести 2 вершины через пробел - запросы")
input_type = input("Для использования файла введить f, для использования ввода с консоли введите c\n")

if input_type == "c":
    n = int(input("Кол-во вершин в дереве: "))
    print("Запишем соединения межлу вершинами (Итерация с нуля):")
    tree = [[] for i in range(n)]
    for i in range(n-1):
        from_, to_ = [int(i) for i in input().split()]
        tree[from_].append(to_)
    m = int(input("Кол-во запросов: "))
    queries = [[] for i in range(n)]
    print("Запросы вводяться аналогично соединениям")
    for i in range(m):
        from_, to_ = [int(i) for i in input().split()]
        queries[from_].append(to_)
        queries[to_].append(from_)

else:
    way = input("Введите путь к вашему файлу: ")
    f = open(way, 'r')
    temp = 0
    for line in f:
        if temp == 0:
            n = int(line)
            tree = [[] for i in range(n)]
            queries = [[] for i in range(n)]
        elif temp < n:
            from_, to_ = [int(i) for i in line.split()]
            tree[from_].append(to_)
        elif temp == n:
            m = int(line)
        elif temp > n:
            from_, to_ = [int(i) for i in line.split()]
            queries[from_].append(to_)
            queries[to_].append(from_)
        temp += 1

dsu = [0]*n
ancestor = [0]*n

visited = [False] * n


def dsu_get(v: int) -> int:
    if dsu[v] != v:
        dsu[v] = dsu_get(dsu[v])
    return dsu[v]


def dsu_union(v: int, u: int):
    v = dsu_get(v)
    u = dsu_get(u)
    if random.randint(0, 1):
        v, u = u, v
    dsu[v] = u
    return u


def dfs(v: int = 0):
    visited[v] = True
    dsu[v] = ancestor[v] = v
    for w in tree[v]:
        if not visited[w]:
            dfs(w)
            leader = dsu_union(v, w)
            ancestor[leader] = v
    for u in queries[v]:
        if visited[u]:
            print(v, u, '->', ancestor[dsu_get(u)])
            queries[u].remove(v)
            queries[v].remove(u)


print("Ответы на запросы: ")

dfs(0)
