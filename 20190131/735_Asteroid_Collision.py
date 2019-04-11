"""
File: 735_Asteroid_Collision.py
Date: 2019/04/11 20:12:28
"""
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        i = 0
        while i < len(asteroids) - 1:
            if asteroids[i] > 0 and asteroids[i+1] < 0:
                if abs(asteroids[i]) == abs(asteroids[i+1]):
                    asteroids.pop(i)
                    asteroids.pop(i)
                    i = i - 1 if i > 0 else i
                elif abs(asteroids[i]) > abs(asteroids[i+1]):
                    asteroids.pop(i+1)
                elif abs(asteroids[i]) < abs(asteroids[i+1]):
                    asteroids.pop(i)
                    i = i - 1 if i > 0 else i
            else:
                i += 1
        return asteroids
                
