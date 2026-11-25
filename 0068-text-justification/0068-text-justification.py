class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        curr_line, curr_line_len = [], 0
        pointer = 0
        res = []
        while pointer<len(words):
            # handle curr_line end
            if (curr_line_len + len(curr_line) + len(words[pointer])) > maxWidth: # (chars in line + spaces required = no. of words + length of current word)
                # handle spaces before appending to result
                all_spaces = maxWidth - curr_line_len
                spaces_words = all_spaces // max(1, len(curr_line)-1)
                extra_spaces = all_spaces % max(1, len(curr_line)-1)
                # append spaces to line.
                for j in range(max(1, len(curr_line)-1)):
                    curr_line[j] += " "*spaces_words
                    if extra_spaces:
                        curr_line[j] += " "
                        extra_spaces-=1
                res.append(''.join(curr_line))
                curr_line, curr_line_len = [], 0
            # append words to curr_line
            curr_line.append(words[pointer])
            curr_line_len+=len(words[pointer])
            pointer+=1
        #handle the last line affter the loop
        last_line = " ".join(curr_line)
        trailing_spaces = maxWidth-len(last_line)
        last_line+=(" "*trailing_spaces)
        res.append(last_line)
        return res
