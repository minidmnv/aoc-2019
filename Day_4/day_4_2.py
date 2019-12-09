input_from = 134564
input_to = 585159

valid_passwords = []

for i in range(input_from, input_to):
    is_valid = True
    same_digits = 0
    same_digits_closed = False
    prev_d = 0
    prev_prev_d = 0
    j = 0
    digits = [int(d) for d in str(i)]

for d in digits:
    if (same_digits == 1 and d != prev_prev_d) or (same_digits == 0 and j == 5 and d == prev_d):
        same_digits_closed = True

if d < prev_d:
    is_valid = False
elif d == prev_d:
    same_digits += 1
elif d != prev_d:
    same_digits = 0

prev_prev_d = prev_d
prev_d = d

j += 1

if is_valid and same_digits_closed:
    valid_passwords.append(i)

print(valid_passwords)
#response
print(len(valid_passwords))