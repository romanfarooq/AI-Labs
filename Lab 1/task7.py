class CountCharacters:
    def count_characters(self, s):
        count = 0
        for char in s:
            if char != ' ':
                count += 1
        return count
    
obj = CountCharacters()

count = obj.count_characters("Roman Farooq")

print(count)