class ReverseWords:
    def reverse_words(self, s):
        words = s.split()
        words.reverse()
        return ' '.join(words)
    
reverse = ReverseWords()

res = reverse.reverse_words("hello .py")

print(res)