"""
Classic Parenthesis Problems

Covers three well-known variants:
  1. Valid Parentheses       - check if a string is balanced
  2. Generate Parentheses    - generate all valid combinations of n pairs
  3. Longest Valid Substring - find length of longest valid parentheses substring
"""

# ---------------------------------------------------------------------------
# 1. Valid Parentheses
#    Given a string containing '(', ')', '{', '}', '[', ']',
#    determine if the input string is valid.
#
#    Approach: stack — push opening brackets, pop and match on closing brackets.
#    Time: O(n)  Space: O(n)
# ---------------------------------------------------------------------------

def is_valid(s: str) -> bool:
    matching = {')': '(', '}': '{', ']': '['}
    stack = []
    for ch in s:
        if ch in matching:
            top = stack.pop() if stack else '#'
            if matching[ch] != top:
                return False
        else:
            stack.append(ch)
    return not stack


# ---------------------------------------------------------------------------
# 2. Generate Parentheses
#    Given n pairs, generate all combinations of well-formed parentheses.
#
#    Approach: backtracking — track open/close counts; add '(' when open < n,
#    add ')' when close < open.
#    Time: O(4^n / sqrt(n))  Space: O(n)  (Catalan number bound)
# ---------------------------------------------------------------------------

def generate_parentheses(n: int) -> list[str]:
    results = []

    def backtrack(current: str, open_count: int, close_count: int):
        if len(current) == 2 * n:
            results.append(current)
            return
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    backtrack('', 0, 0)
    return results


# ---------------------------------------------------------------------------
# 3. Longest Valid Parentheses
#    Given a string of '(' and ')', find the length of the longest valid
#    (well-formed) parentheses substring.
#
#    Approach: stack storing indices — keep a base index (-1) for tracking
#    the start of the current valid window.
#    Time: O(n)  Space: O(n)
# ---------------------------------------------------------------------------

def longest_valid_parentheses(s: str) -> int:
    max_len = 0
    stack = [-1]  # base index

    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)  # new base
            else:
                max_len = max(max_len, i - stack[-1])

    return max_len


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    # --- Valid Parentheses ---
    print("=== Valid Parentheses ===")
    test_cases = ['()', '()[]{}'  , '(]', '([)]', '{[]}', '', '((']
    for t in test_cases:
        print(f"  {t!r:12} -> {is_valid(t)}")

    # --- Generate Parentheses ---
    print("\n=== Generate Parentheses ===")
    for n in range(1, 4):
        combos = generate_parentheses(n)
        print(f"  n={n} ({len(combos)} combos): {combos}")

    # --- Longest Valid Parentheses ---
    print("\n=== Longest Valid Parentheses ===")
    lv_cases = [
        ('(()',        2),
        (')()())',     4),
        ('',           0),
        ('()()',       4),
        ('(())',       4),
        ('()(()',      2),
        ('(((((',      0),
    ]
    for s, expected in lv_cases:
        result = longest_valid_parentheses(s)
        status = 'OK' if result == expected else f'FAIL (expected {expected})'
        print(f"  {s!r:12} -> {result}  {status}")
