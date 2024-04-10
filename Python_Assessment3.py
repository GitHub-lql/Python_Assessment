def sort_table(table, k):
    return sorted(table, key=lambda x: x[k])


if __name__ == '__main__':
    n, m = map(int, input().split())

    table = []
    for _ in range(n):
        table.append(list(map(int, input().rstrip().split())))

    k = int(input())

    sorted_table = sort_table(table, k)

    for row in sorted_table:
        print(' '.join(map(str, row)))
