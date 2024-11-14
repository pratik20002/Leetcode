from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # Handle the case when the asteroid is positive
            if asteroid > 0:
                stack.append(asteroid)
            else:
                # While there are positive asteroids and the current negative asteroid can destroy them
                while stack and stack[-1] > 0:
                    # If the current negative asteroid destroys a positive asteroid completely
                    if stack[-1] == -asteroid:
                        stack.pop()
                        break
                    # If the current negative asteroid destroys a positive asteroid partially
                    elif stack[-1] < -asteroid:
                        stack.pop()
                    # If the current negative asteroid gets destroyed by a positive asteroid
                    else:
                        break
                else:
                    # If there are no positive asteroids to destroy the current negative asteroid
                    stack.append(asteroid)

        return stack
