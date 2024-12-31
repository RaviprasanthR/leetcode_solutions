# 13. Roman to Integer

def romanToInt(self, s: str) -> int:
    ref = {'I' : 1, 'V' : 5, 'X': 10, 'L': 50, 'C' : 100, 'D': 500, 'M': 1000}
    acc = 0
    prev_val = 0
    for i in range(len(s)-1,-1,-1):
        curr_val = ref[s[i]]
        if curr_val >= prev_val:
            acc += curr_val
        else:
            acc -= curr_val
        prev_val = curr_val
    return acc