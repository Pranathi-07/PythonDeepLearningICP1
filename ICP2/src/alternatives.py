def string_alternative(str) :
    alts = str[::2]
    return alts
if __name__ == "__main__":
    str = input("Enter the string: ")
    alter = string_alternative(str)
    print(alter)
