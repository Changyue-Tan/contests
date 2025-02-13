# suppose tohave bug, cannot find it 
# do not what is the test case to involk the bug

def find_pair_with_sum(n, target, ropes):
    # Store ropes in a set for O(1) average time complexity checks
    ropes_set = set(ropes)

    for a in ropes_set:
        b = target - a
        if b in ropes_set:
            print("YES")
            print(a, b)
            return

    print("NO")

# Reading input
n, target = map(int, input().split())
ropes = list(map(int, input().split()))

find_pair_with_sum(n, target, ropes)
