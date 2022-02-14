class Solution(object):
    def changeDirection(self, current_direction, instruction):
        # north only
        if current_direction == "N" and instruction == "G":
            current_direction = "N"
        elif current_direction == "N" and instruction == "L":
            current_direction = "W"
        elif current_direction == "N" and instruction == "R":
            current_direction = "E"
            
        # south only
        elif current_direction == "S" and instruction == "G":
            current_direction = "S"
        elif current_direction == "S" and instruction == "L":
            current_direction = "E"
        elif current_direction == "S" and instruction == "R":
            current_direction = "W"
            
        # east only
        elif current_direction == "E" and instruction == "G":
            current_direction = "E"
        elif current_direction == "E" and instruction == "L":
            current_direction = "N"
        elif current_direction == "E" and instruction == "R":
            current_direction = "S"
            
        # west only
        elif current_direction == "W" and instruction == "G":
            current_direction = "W"
        elif current_direction == "W" and instruction == "L":
            current_direction = "S"
        elif current_direction == "W" and instruction == "R":
            current_direction = "N"
            
        return current_direction  
        
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        
        # edge cases
        if set(instructions) == {"G"}:
            return False
        elif set(instructions) == {"L"} or set(instructions) == {"L"} or set(instructions) == {"L", "R"}:
            return True
        
        # kepp track of current direction
        current_direction = "N"
        position = [0, 0]
        
        for _ in range(len(instructions)*2):
            for i in instructions:
                # check direction based on instruction
                current_direction = self.changeDirection(current_direction, i)
                # increment or decrement x, y accordingly
                if current_direction == "N" and i == "G":
                    position[1]+=1
                elif current_direction == "S" and i == "G":
                    position[1]-=1
                elif current_direction == "E" and i == "G":
                    position[0]+=1
                elif current_direction == "W" and i == "G":
                    position[0]-=1
            if position == [0, 0]:
                return True
        
