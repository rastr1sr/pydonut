import math
import time

def main():
    A, B = 0, 0
    while True:
        z = [0] * 1760
        b = [' '] * 1760
        for j in range(0, 628, 7):  
            sin_j = math.sin(j / 100)
            cos_j = math.cos(j / 100)
            for i in range(0, 628, 2):  
                sin_i = math.sin(i / 100)
                cos_i = math.cos(i / 100)
                e, f, g = math.sin(A), sin_j, math.cos(A)
                h = cos_j + 2
                D = 1 / (sin_i * h * e + f * g + 5)
                l, m, n = cos_i, math.cos(B), math.sin(B)
                t = sin_i * h * g - f * e
                x = int(40 + 30 * D * (l * h * m - t * n))
                y = int(12 + 15 * D * (l * h * n + t * m))
                o = int(x + 80 * y)
                N = int(8 * ((f * e - sin_i * cos_j * g) * m - sin_i * cos_j * e - f * g - l * cos_j * n))
                if 0 <= y < 22 and 0 <= x < 80 and D > z[o]:
                    z[o], b[o] = D, ".,-~:;=!*#$@"[max(0, N)]

        print("\033[H", end="")
        print(''.join(b[k] if k % 80 else b[k] + '\n' for k in range(1760)))
        A, B = A + 0.04, B + 0.02
        time.sleep(0.03)

if __name__ == "__main__":
    main()
