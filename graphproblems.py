import collections
import helper

m = collections.namedtuple('match', ('team_a', 'team_b'))


# O(matches)
def can_team_a_beat_b(matches: [m], teama: str, teamb: str) -> bool:
    def is_path_dfs(curr: str, visited=None) -> bool:
        if visited is None:
            visited = set()
        if curr == teamb:
            return True
        elif curr not in g or curr in visited:
            return False
        visited.add(curr)
        return any(is_path_dfs(d, visited) for d in g[curr])

    g = collections.defaultdict(set)
    for match in matches:
        g[match.team_a].add(match.team_b)
    return is_path_dfs(teama)


# print(can_team_a_beat_b([m('A', 'B'), m('B', 'C'), m('C', 'D'), m('D', 'E')], 'A', 'E'))

BLACK, WHITE = range(2)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
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


# print(searchmaze(coordinate(0, 0), coordinate(len(maze) - 1, len(maze[len(maze) - 1]) - 1)))


def flip_maze_bfs(c: coordinate) -> None:
    color = maze[c.x][c.y]  # original color
    q = collections.deque([c])  # add staring coordinate to the queue
    maze[c.x][c.y] = 1 - maze[c.x][c.y]  # flip color
    while q:
        curr = q.popleft()
        for adj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            n = coordinate(curr.x + adj[0], curr.y + adj[1])
            if 0 <= n.x < len(maze) and 0 <= n.y < len(maze[n.x]) and maze[n.x][n.y] == color:
                q.append(n)
                maze[n.x][n.y] = 1 - maze[n.x][n.y]


def flip_maze_dfs(c: coordinate) -> None:
    color = maze[c.x][c.y]
    maze[c.x][c.y] = 1 - color
    for adj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        n = coordinate(c.x + adj[0], c.y + adj[1])
        if 0 <= n.x < len(maze) and 0 <= n.y < len(maze[n.x]) and maze[n.x][n.y] == color:
            flip_maze_dfs(n)


# s: coordinate = coordinate(0, 0)
# helper.pm(maze)
# flip_maze_bfs(s)
# helper.pm(maze)
# flip_maze_dfs(s)
# helper.pm(maze)


board = [['B', 'B', 'B', 'B'],
         ['W', 'W', 'W', 'B'],
         ['B', 'W', 'W', 'B'],
         ['B', 'B', 'B', 'B']]


# find 'W' not reachable from the edge and color them 'B'.
# Start with edge items colored 'W'
def fill_enclosed_region() -> [[chr]]:
    n, m = len(board), len(board[0])
    q = collections.deque([])
    # add border elements to the queue
    for i in range(0, n):
        q.append((i, 0))
        q.append((i, m - 1))
    for j in range(0, m):
        q.append((0, j))
        q.append((j, n - 1))
    # print(q)

    while q:
        curr = q.popleft()
        x, y = curr[0], curr[1]
        # All valid edge items with 'W'
        if 0 <= x < n and 0 <= y < m and board[x][y] == 'W':
            board[x][y] = 'T'
            # add adjacent elements of this 'W' item
            for adj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                q.append((x + adj[0], y + adj[1]))
        helper.pm(board)
    return [['B' if board[i][j] != 'T' else 'W' for j in range(0, m)] for i in range(0, n)]

# helper.pm(board)
# helper.pm(fill_enclosed_region())
