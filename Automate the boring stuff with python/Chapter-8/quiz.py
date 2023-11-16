import random, time

num_q = 10
correct_ans = 0
check_c = 0
correct = 0

for i in range(num_q):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    correct_ans = n1 * n2
    prompt = f'{i + 1}: {n1} x {n2} = '
    check_c = 0
    t1 = int(time.time())
    while check_c < 3:
        ans = int(input(f'{prompt}'))

        t2 = int(time.time())
        elapsedTime = t2 - t1
        if elapsedTime > 8:
            print("Out of time!")
            break
        if ans == correct_ans:
            correct += 1
            print('Correct!')
            time.sleep(1)
            break
        else:
            check_c += 1
    if check_c == 3:
        print('Incorrect')

print(f'score = {correct} out of {num_q}')
