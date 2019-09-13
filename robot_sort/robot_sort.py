class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # The bubble sort algorithm would be helpful to write this function.
        # How?
        
        # Robot compares each item in the list to the next one. If item in position i is higher than
        # item in position i + 1, robot swaps them. You can check you're finished with can_move_right
        # method.

        # If there was a swap, you turn the robot's light on. If light is on at the end of the list,
        # you start all over again from the start of the list until light is off at the end of list.

        # ******************************************************************

        # Take the first item

        # Set light on to enter while loop
        self.set_light_on()

        # Loop until no swaps are made
        while self.light_is_on() == True:

            # Sets initial state to no swaps 
            self.set_light_off()

            # Takes robot to beginning of list
            while self.can_move_left() == True:
                self.move_left()
            
            # Pick first item
            self.swap_item()

            # Begin loop until end of list
            while self.can_move_right() == True:
            
                self.move_right()

                if self.compare_item() == 1:
                    # If next item is smaller, swap them and turn light on
                    self.swap_item()
                    self.set_light_on()
                    # Then go back and leave the other item behind, swap it for None.
                    self.move_left()
                    self.swap_item()
                    # Then return to previous position and grab item
                    self.move_right()
                    self.swap_item()
            
                # If it's equal, go back, leave the item and take the next one
                elif self.compare_item == 0:
                    # Then go back and leave the other item behind, swap it for None.
                    self.move_left()
                    self.swap_item()
                    # Then return to previous position and grab item
                    self.move_right()
                    self.swap_item()

                else:
                    # If it's bigger, go back and leave the item in it's place
                    self.move_left()
                    self.swap_item()
                    # And then take the next item to start the loop again
                    self.move_right()
                    self.swap_item()
            
            self.swap_item()



if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [5, 4, 3, 2, 1]
    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)