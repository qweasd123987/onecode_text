import heapq
import random

class MazeSolver:
    def __init__(self, maze, start, goal):
        self.maze = maze
        self.start = start
        self.goal = goal
        self.rows = len(maze)
        self.cols = len(maze[0])

    def in_bounds(self, pos):
        r, c = pos
        return 0 <= r < self.rows and 0 <= c < self.cols

    def passable(self, pos):
        r, c = pos
        return self.maze[r][c] == 0

    def neighbors(self, pos):
        r, c = pos
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        result = []
        for dr, dc in directions:
            new = (r+dr, c+dc)
            if self.in_bounds(new) and self.passable(new):
                result.append(new)
        return result

    def reconstruct_path(self, came_from):
        cur = self.goal
        path = []
        while cur != self.start:
            path.append(cur)
            cur = came_from[cur]
        path.append(self.start)
        return path[::-1]

    def bfs(self):
        from collections import deque
        queue = deque([self.start])
        came_from = {self.start: None}
        while queue:
            cur = queue.popleft()
            if cur == self.goal:
                return self.reconstruct_path(came_from)
            for nxt in self.neighbors(cur):
                if nxt not in came_from:
                    queue.append(nxt)
                    came_from[nxt] = cur
        return None

    def dfs(self):
        stack = [self.start]
        came_from = {self.start: None}
        while stack:
            cur = stack.pop()
            if cur == self.goal:
                return self.reconstruct_path(came_from)
            for nxt in self.neighbors(cur):
                if nxt not in came_from:
                    stack.append(nxt)
                    came_from[nxt] = cur
        return None

    def heuristic(self, a, b):
        # 曼哈顿距离
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    def astar(self):
        frontier = []
        heapq.heappush(frontier, (0, self.start))
        came_from = {self.start: None}
        cost_so_far = {self.start: 0}
        while frontier:
            _, cur = heapq.heappop(frontier)
            if cur == self.goal:
                return self.reconstruct_path(came_from)
            for nxt in self.neighbors(cur):
                new_cost = cost_so_far[cur] + 1
                if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                    cost_so_far[nxt] = new_cost
                    priority = new_cost + self.heuristic(nxt, self.goal)
                    heapq.heappush(frontier, (priority, nxt))
                    came_from[nxt] = cur
        return None

    def visualize(self, path):
        grid = [row[:] for row in self.maze]  # 复制
        for r,c in path:
            grid[r][c] = "*"
        grid[self.start[0]][self.start[1]] = "S"
        grid[self.goal[0]][self.goal[1]] = "G"
        for row in grid:
            print("".join(str(x) for x in row))


if __name__ == "__main__":
    # 0=路，1=墙
    maze = [
        [0,0,1,0,0,0],
        [1,0,1,0,1,0],
        [0,0,0,0,1,0],
        [0,1,1,0,0,0],
        [0,0,0,1,1,0],
        [0,1,0,0,0,0]
    ]

    start = (0,0)
    goal = (5,5)

    solver = MazeSolver(maze, start, goal)

    print("BFS路径：")
    path_bfs = solver.bfs()
    solver.visualize(path_bfs)
    print("\nDFS路径：")
    path_dfs = solver.dfs()
    solver.visualize(path_dfs)
    print("\nA*路径：")
    path_astar = solver.astar()
    solver.visualize(path_astar)
