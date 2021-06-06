class PalindromeString(str): # subclass of str class

    def is_palindrome(self):
        i = 0
        j = len(self) - 1
        while i < j:
            if self[i] != self[j]:
                return False
            i = i + 1
            j = j -1
        return True

if __name__ == "__main__":
    word = PalindromeString("radar")
    word2 = PalindromeString("radar")
    print(f"{word} length is {len(word)} and uppecase is {word.upper()}")
    print(f"{word} {word.is_palindrome()}")
    print(f"{word2} length is {len(word2)} and uppecase is {word2.upper()}")
    print(f"{word2} {word2.is_palindrome()}")