def can_cut(circumference):
    if circumference >= 50:
        return True
    else:
        return False



circumference = int(input('Enter tree circumference in cm: '))
if (can_cut(circumference)):
    print("A tree can be cut down")
else:
    print("A tree cannot be cut down")

trees = [ 160, 90, 230, 120]

index = 0
for tree in trees:
    index += 1
    print(f"Tree #{index}: {can_cut(tree)}")
