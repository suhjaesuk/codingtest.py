rice_cake_count, required_rice_cake_height = map(int, input().split())
rice_cake = list(map(int, input().split()))

def solve_cutter_height(required_rice_cake_height, rice_cake):
    rice_cake.sort()
    cutter = rice_cake[0]
    while cutter <= rice_cake[-1]:
        temp = 0
        for i in rice_cake:
            if cutter < i:
                temp = temp + (i - cutter)
        if temp == required_rice_cake_height:
            return cutter
        cutter += 1

print(solve_cutter_height(required_rice_cake_height, rice_cake))



