class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        for the easy question i used a stack and it feels like i can replicate it over
        here as well, we solved that by having a stack to keep track of opening brackets
        and when we encounter a closing bracket we pop until either we have equal amounts
        or one is greater than the other in which case we return false

        one stack might not be enough in this case coz a star can be both right and left
        brackets as well as an "" empty string meaning can ignore it

        so have one stack for left brackets, another for the stars and we keep track of
        their indexes? yeah coz u need the place of where a star is to see if we can do 
        anythign with it

        so one stack for opening brackets ( and one for stars *

        when we see a left bracket or star we insert into their respective arrays

        when we see a right bracket remove from left bracket first. There are 2 subcases

        1) if left runs out then remove from star but see that star index is less than
        right index

        2) if left remains in the end, then remove from star but see that star index is
        greater than left index
        """
        left_stack = []
        star_stack = []

        for i in range(len(s)):
            if s[i] == '(':
                left_stack.append(i)
            elif s[i] == '*':
                star_stack.append(i)
            else:
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        
        if not left_stack:
            return True
        
        while left_stack and star_stack:
            left_index = left_stack.pop()
            star_index = star_stack.pop()

            if star_index < left_index:
                return False
        
        return not left_stack
        





















