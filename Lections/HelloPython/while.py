# Управляющие конструкции:
# while

# while condition:
#  # operator 1
#  # operator 2
#  # . . .
#  # operator n

original = 23
inverted = 0
while original != 0:
 inverted = inverted * 10 + (original % 10)
 original //= 10
print(inverted)