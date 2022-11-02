import collections

m = collections.namedtuple('match', ('team_a', 'team_b'))


# O(matches)
def can_team_a_beat_b(matches: [m], teama: str, teamb: str) -> bool:
    def is_path_dfs(curr: str, target: str, visited=None) -> bool:
        if visited is None:
            visited = set()
        if curr == target:
            return True
        elif curr not in g or curr in visited:
            return False
        visited.add(curr)
        return any(is_path_dfs(d, target, visited) for d in g[curr])

    g = collections.defaultdict(set)
    for match in matches:
        g[match.team_a].add(match.team_b)
    return is_path_dfs(teama, teamb)


# print(can_team_a_beat_b([m('A', 'B'), m('B', 'C'), m('C', 'D'), m('D', 'E')], 'A', 'E'))

BLACK, WHITE = range(2)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

coordinate = collections.namedtuple('coordinate', ('x', 'y'))


def searchmaze(s: coordinate, e: coordinate) -> [coordinate]:
    def helper(c: coordinate) -> bool:
        if not (0 <= c.x < len(maze) and 0 <= c.y < len(maze[c.x]) and maze[c.x][c.y] == WHITE):
            return False
        path.append(c)
        maze[c.x][c.y] = BLACK
        if c == e:
            return True
        if any(map(helper, (
                coordinate(c.x + 1, c.y), coordinate(c.x - 1, c.y), coordinate(c.x, c.y - 1),
                coordinate(c.x, c.y + 1)))):
            return True
        # cannot find a path, remove the entry added in path.append(cur),
        del path[-1]
        return False

    path: [coordinate] = []
    if not helper(s):
        return []
    return path


print(searchmaze(coordinate(0, 0), coordinate(len(maze) - 1, len(maze[len(maze) - 1]) - 1)))
