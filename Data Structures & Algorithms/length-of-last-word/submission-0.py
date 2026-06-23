class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cursor = 0
        in_string = False
        string_start = 0
        prev_word_length = 0
        while cursor < len(s):
            if s[cursor] == ' ':
                if in_string:
                    prev_word_length = cursor - string_start
                    in_string = False
                cursor += 1
            else:
                if not in_string:
                    string_start = cursor
                    in_string = True
                cursor += 1
        if in_string:
            prev_word_length = cursor - string_start
        return prev_word_length