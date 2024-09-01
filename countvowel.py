#Function count_vowel
def count_vowels(text):
    vowels = 'aeiou'
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

if __name__ == "__main__":
    
    text = "Hello, World!"
    print(count_vowels(text))  

