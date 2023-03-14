# FOR loops
rows = 5
cols = 5

def plaintext_bottomleft():
    print("\nPlain text output:")
    print("*")
    print("**")
    print("***")
    print("****")
    print("*****")

def string_bottomleft():
    print("\nPrint a bottom-left triangle using string operations.")
    for i in range(rows):
        print("*" * (i+1))

def string_topleft():
    print("\nPrint a top-left triangle using string operations.")
    for i in range(rows):
        print("*" * (rows-i))

def string_bottomright():
    print("\nPrint a bottom-right triangle using string operations.")
    for i in range(rows):
        print(" " * (rows-i-1) + "*" * (i+1))

def string_topright():
    print("\nPrint a top-right triangle using string operations.")
    for i in range(rows):
        print(" " * i + "*" * (rows-i))

def loop1_bottomleft():
    print("\nPrint a bottom-left triangle using FOR loop.")
    for i in range(rows):
        for j in range(cols):
            if (j <= i):
                print("*", end="")
        print()

def diamond_loop():
    print("\nPrint diamond patterns using FOR loop.")
    for i in range(20):
        for j in range(20):
            if ((i+j) % 10 <= 5):
                print("##", end="")
            else:
                print("  ", end="")
        print()

#plaintext_bottomleft()
#string_bottomleft()
#string_topleft()
#string_bottomright()
#string_topright()
#loop1_bottomleft()
diamond_loop()