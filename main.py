try:
    a1 = int(input("->"))
    b1 = int(input("->"))

    def print_rec(a, b):
        for i in range(0, a):
            for j in range(0, b):
                print("/", end=" ")
            print()
        print()


    def main():
        print_rec(a1, b1)


    main()

except Exception as ex:
    print(f'Error', {ex})
