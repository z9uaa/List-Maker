import random
import time
import string
print('Program By Flxr | Instagram : 1ee_')

def g (w = 3):
    le = string.ascii_letters
    return ''.join((random.choice(le) for i in range(w)))

flxr_filename = input('Enter Name File: ')
flxr_letters = input('How many letters: ')
flxr_many = input('How many do you want:')

with open(f'{flxr_filename}''.txt', 'w') as f:
    start = time.time()
    for x in range(int(flxr_many)):
        f.write(g(int(flxr_letters)) + '\n')

print("Done Saved")
input("Press Enter To Exit : ")
