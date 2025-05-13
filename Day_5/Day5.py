# 1
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

print(sum(student_scores))
print(max(student_scores))

# Sum
total = 0
for total_score in student_scores:
    total += total_score
print(total)

# Max
maks = 0
for max_score in student_scores:
    if maks < max_score:
        maks = max_score

print(maks)

#FizzBuzz
for fizzbuzz in range(1,101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("FizzBuzz")
    elif fizzbuzz % 3 == 0:
        print("Fizz")
    elif fizzbuzz % 5 == 0:
        print("Buzz")