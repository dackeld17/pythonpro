def frequency_analytic(s):
    dictionary = {}

    for char in s:
        if char.isspace():
            continue
        dictionary[char] = dictionary.get(char, 0) + 1
       
    for char, frequency in dictionary.items():
         print(f"{char} {frequency}")

if __name__ == "__main__":
    msg = input("input your message : ")
    frequency_analytic(msg)

