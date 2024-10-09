print ("Program Aritmatika".upper())

def deret_aritmatika(N):
    awal = 2
    beda = 3
    hasil = [awal + i * beda for i in range(N)]
    return hasil

# Penggunaan
N = int(input("Input : "))
print(f"Output: {{ {', '.join(map(str, deret_aritmatika(N)))} }}")
