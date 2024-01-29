gryffindor = set(input().split())
ravenclaw = set(input().split())
slytherin = set(input().split())
hufflepuff = set(input().split())

# Combine all student sets using the union operator
all_students = gryffindor | ravenclaw | slytherin | hufflepuff

# Print the resulting set
print(all_students)