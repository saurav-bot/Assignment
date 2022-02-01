def first_digit(num):
    odd_sum = 0

    for i in range(len(num)-1, -1, -2):
        odd_sum += int(num[i])

    return odd_sum


def second_digit(num):
    even_sum = 0

    for i in range(len(num)-2, -1, -2):
        temp = int(num[i])*2
        if temp > 9:
            even_sum += (temp%10 + 1)
        else:
            even_sum += temp

    return even_sum


def c_length(num):
    length = len(num)
    if length >= 13 and length <=16:
        if num[0] == "4" or num[0] == "5" or num[0] == "6" or (num[0] == "3" and num[1] == "7"):
            return True
    return False


def validator(card_number):
    
    total = first_digit(card_number) + second_digit(card_number)
    
    card_length = c_length(card_number)

    if total % 10 == 0 and card_length:
        return True 
    
    return False

if __name__ == "__main__":
    number = input("Enter your credit card number to validate: ")
    print(validator(number))