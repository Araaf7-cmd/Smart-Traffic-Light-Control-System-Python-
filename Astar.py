from collections import deque

def is_valid_state(state, N):
    m_left, c_left, boat = state
    m_right = N - m_left
    c_right = N - c_left
    if not (0 <= m_left <= N and 0 <= c_left <= N):
        return False
    if m_left > 0 and c_left > m_left:
        return False
    if m_right > 0 and c_right > m_right:
        return False
    return True

def successors(state, N, boat_capacity=2):
    m_left, c_left, boat = state
    moves = []
    if boat == 1:
        max_m = min(m_left, boat_capacity)
        max_c = min(c_left, boat_capacity)
        for m in range(0, max_m+1):
            for c in range(0, max_c+1):
                if 1 <= m + c <= boat_capacity:
                    new_state = (m_left - m, c_left - c, 0)
                    if is_valid_state(new_state, N):
                        moves.append(new_state)
    else:
        m_right = N - m_left
        c_right = N - c_left
        max_m = min(m_right, boat_capacity)
        max_c = min(c_right, boat_capacity)
        for m in range(0, max_m+1):
            for c in range(0, max_c+1):
                if 1 <= m + c <= boat_capacity:
                    new_state = (m_left + m, c_left + c, 1)
                    if is_valid_state(new_state, N):
                        moves.append(new_state)
    return moves

def bfs_solve(N=3, boat_capacity=2):
    start = (N, N, 1)
    goal  = (0, 0, 0)
    queue = deque([start])
    parent = {start: None}
    while queue:
        state = queue.popleft()
        if state == goal:
            path = []
            s = state
            while s is not None:
                path.append(s)
                s = parent[s]
            return path[::-1]
        for succ in successors(state, N, boat_capacity):
            if succ not in parent:
                parent[succ] = state
                queue.append(succ)
    return None

def print_solution(path):
    def side(b): return 'L' if b==1 else 'R'
    for i, (m, c, b) in enumerate(path):
        print(f"Step {i}: Left(M={m}, C={c}), Boat={side(b)}")
    print(f"Total moves: {len(path)-1}")

if __name__ == "__main__":
    path = bfs_solve(3, 2)
    if path:
        print_solution(path)
    else:
        print("No solution found.")
