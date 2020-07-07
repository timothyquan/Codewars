def solution(number):
    num1, num2 = 3, 5
    found_multiples = []
    for i in range(num1, number, num1):
        found_multiples.append(i)
    for i in range(num2, number, num2):
        found_multiples.append(i)

    return sum(set(found_multiples))


input_num = int(input("Input the top range number:"))
print(solution(input_num))
