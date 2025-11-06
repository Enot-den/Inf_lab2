def Hemming_code(nums):
    s1 = (nums[0] + nums[2] + nums[4] + nums[6]) % 2
    s2 = (nums[1] + nums[2] + nums[5] + nums[6]) % 2
    s3 = (nums[3] + nums[4] + nums[5] + nums[6]) % 2
    if s1+s2+s3==0:
        print("нет ошибок")
        return nums
    ErrNum = s1 + 2 * s2 + 4 * s3
    ErrS = ["r1", "r2", "i1", "r3", "i2", "i3", "i4"][ErrNum - 1]
    print(f"Ошибка в {ErrNum}-ом бите кодового слова ({ErrS})")
    nums[ErrNum-1] = abs(nums[ErrNum-1] - 1)
    return nums

while True:
    print('Для выхода напишите "exit"')
    x = input("Введите сообщение без пробелов: ")
    while not(set(x) <= {"0", "1"}):
        if x == "exit":
            break
        print("Ошибочный ввод. Допустимые символы: 0, 1")
        x = input("Введите сообщение: ")
    if x == "exit":
        break
    N = list(map(int, list(x)))

    r = Hemming_code(N)
    print(f"Правильное сообщение: {r[2]}{r[4]}{r[5]}{r[6]}\n")


