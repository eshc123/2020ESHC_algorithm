class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum(): # 영문자, 숫자 판별, 문자이면 True 반환
                strs.append(char.lower())
        if strs==strs[::-1]:
            return True
        else :
            False
# isalnum() 은 영문자, 숫자 여부를 판별하는 함수, 영문자이면 true를 반환