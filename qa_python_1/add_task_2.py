def digit_root(num):
    sum = 0
    if num < 10:
        print (num)
        return num
    else:
        while num > 9:
            sum += num % 10
            print(sum)
            num = num // 10
        sum += num
        return digit_root(sum)

number = 12345
print(digit_root(number))