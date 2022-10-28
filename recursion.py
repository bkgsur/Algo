def n_queen(n: int) -> [[int]]:
    def helper(row):
        if row == n:
            result.append(list(col_placement))
            return
        else:
            for col in range(n):
                if all(abs(col-c) not in (0, row - i) for i, c in enumerate(col_placement[:row])):
                    col_placement[row] = col
                    helper(row + 1)

    result: [[int]] = []
    col_placement: [int] = [0] * n
    # start with first row
    helper(0)
    return result


print(n_queen(4))
