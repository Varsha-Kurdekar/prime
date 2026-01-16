def get_prime_details():
    num = int(input("Enter a number: "))
    if num <= 1:
        return num, False
    for i in range(2, num):
        if num % i == 0:
            return num, False
    return num, True
def display_prime_details(num, is_prime):
    print("Number details:")
    if is_prime:
        print("Number is prime:", num)
    else:
        print("Number is not prime:", num)
if __name__ == "__main__":
    num, prime = get_prime_details()
    display_prime_details(num, prime)