import collections


def pm(a):
    s = [[str(e) for e in row] for row in a]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))
    print('=============================')


e = collections.namedtuple('e', ('v1', 'v2'))


class vertex:
    WHITE, GRAY, BLACK = range(3)

    def __init__(self, n):
        self.color = self.WHITE
        self.n = n
        self.edges = []

    def __eq__(self, another):
        return hasattr(another, 'n') and self.n == another.n

    def __hash__(self):
        return hash(self.n)


def buildgraph() -> dict:
    g = collections.defaultdict(set)
    g[vertex('A')].add(vertex('B'))
    g[vertex('B')].add(vertex('C'))
    g[vertex('B')].add(vertex('D'))
    g[vertex('B')].add(vertex('E'))
    g[vertex('D')].add(vertex('E'))
    g[vertex('D')].add(vertex('B'))
    g[vertex('E')].add(vertex('B'))
    g[vertex('E')].add(vertex('D'))
    return dict(g)


def buildgraph2() -> vertex:
    a = vertex('A')
    b = vertex('B')
    c = vertex('C')
    d = vertex('D')
    e1 = vertex('E')
    a.edges.append(b)
    b.edges.append(c)
    b.edges.append(d)
    b.edges.append(e1)
    d.edges.append(b)
    # d.edges.append(e)
    # e.edges.append(b)
    # e.edges.append(d)
    return a


def printgraph(g: vertex) -> None:
    if not g:
        return ''
    n = [g.n]
    q = collections.deque([g])
    seen = set(g.n)
    while q:
        v = q.popleft()
        print(seen)
        for edge in v.edges:
            if edge.n not in seen:
                n.append(edge.n)
                q.append(edge)
                seen.add(edge.n)

    print('->'.join(n))
