input_from = 134564
input_to = 585159

valid_passwords = []

for i in range(input_from, input_to):
    is_valid = True
    same_digits = False
    prev_d = 0
    digits = [int(d) for d in str(i)]

for d in digits:
    if d < prev_d:
        is_valid = False
    elif d == prev_d:
        same_digits = True
    prev_d = d

if is_valid and same_digits:
    valid_passwords.append(i)

print(valid_passwords)
print(len(valid_passwords))