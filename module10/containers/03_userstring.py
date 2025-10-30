from collections import UserString


class SmartString(UserString):
    def is_palindrome(self):
        return self.data[::-1] == self.data

    def lower(self):
        self.data += "!"
        return super().lower()


s = SmartString("abba")
print(s.is_palindrome())
print(s.lower())
