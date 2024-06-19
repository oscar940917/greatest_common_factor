def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def main():
    a, b = map(int, input().split())
    result = gcd(a, b)
    print(result)
if __name__ == "__main__":
    main()
