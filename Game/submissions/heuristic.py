def my_agent(obs, config):
    import random
    import numpy as np
    
    def score_move(grid, col, mark, config):
        next_grid = drop_piece(grid, col, mark, config)
        score = get_heuristic(next_grid, mark, config)
        return score

    def drop_piece(grid, col, mark, config):
        next_grid = grid.copy()
        for row in range(config.rows-1, -1, -1):
            if next_grid[row][col] == 0:
                break
        next_grid[row][col] = mark
        return next_grid

    def get_heuristic(grid, mark, config):
        num_threes = count_windows(grid, 3, mark, config)
        num_fours = count_windows(grid, 4, mark, config)
        num_threes_opp = count_windows(grid, 3, mark%2+1, config)
        score = num_threes + 1e6*num_fours - 1e2*num_threes_opp
        return score

    def check_window(window, num_discs, piece, config):
        return (window.count(piece) == num_discs
               and window.count(0) == config.inarow - num_discs)

    def count_windows(grid, num_discs, piece, config):
        num_windows = 0
        for row in range(config.rows):
            for col in range(config.columns - (config.inarow - 1)):
                window = list(grid[row, col:col+config.inarow])
                if check_window(window, num_discs, piece, config):
                    num_windows += 1
        for row in range(config.rows - (config.inarow - 1)):
            for col in range(config.columns):
                window = list(grid[row:row+config.inarow, col])
                if check_window(window, num_discs, piece, config):
                    num_windows += 1
        for row in range(config.rows - (config.inarow - 1)):
            for col in range(config.columns - (config.inarow - 1)):
                window = list(grid[range(row, row-config.inarow, -1),
                                  range(col, col+config.inarow)])
                if check_window(window, num_discs, piece, config):
                    num_windows += 1
        return num_windows
    
    valid_moves = [c for c in range(config.columns)
                  if obs.board[c] == 0]
    grid = np.asarray(obs.board).reshape(config.rows, config.columns)
    scores = dict(zip(valid_moves, 
                      [score_move(grid, col, obs.mark, config)
                      for col in valid_moves]))
    max_cols = [key for key in scores.keys()
               if scores[key] == max(scores.values())]
    return random.choice(max_cols)
