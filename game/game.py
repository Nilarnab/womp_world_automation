class World:
    def __init__(self):
        # making self.chart
        # -2 means: monster, -1 means pit, 1 means gold
        self.conv = {-2: 'MONSTER', -1: 'PIT', 0: 'VOID', 1: 'GOLD'}
        self.chart = [[0 for i in range(4)] for j in range(4)]

        # placing monster
        self.chart[2][0] = -2

        # placing pits
        self.chart[0][2] = self.chart[2][2] = self.chart[3][3] = -1

        # placing Gold
        self.chart[2][1] = 1

        print("Gaming environment created")
        for i in range(len(self.chart)):
            for j in range(len(self.chart[i])):
                print(self.conv[self.chart[i][j]], end=" ")
            print("")

    def is_safe(self, position):
        """
        Returns True if the agent is alive after reaching this position
        :param position: [xth row, yth column]
        :return: bool: True if alive
        """
        if self.chart[position[0]][position[1]] < 0:
            return False
        else:
            return True

    def is_successful(self, position):
        """
        Returns True if the agent has found gold after reaching this position
        :param position: [xth row, yth column]
        :return: bool: True if gold is found
        """
        # return False
        if self.chart[position[0]][position[1]] == 1:
            return True
        else:
            return False

    def is_valid(self, position):
        """
        Returns true if the position is valid
        :param position:
        :return: bool
        """

        # print("position received", position)

        if 0 <= position[0] < 4 and 0 <= position[1] < 4:
            # print("Valid")
            return True
        else:
            return False

    def get_state(self, position):
        """
        Function to return the state of a given position
        :param position: [xth row, yth column]
        :return: bool list[is_safe, stench, breeze]
        """
        required_pos = []
        state = [0 for i in range(3)]

        if self.is_valid([position[0] - 1, position[1]]):
            required_pos.append([position[0] - 1, position[1]])

        if self.is_valid([position[0], position[1] + 1]):
            required_pos.append([position[0], position[1] + 1])

        if self.is_valid([position[0] + 1, position[1]]):
            required_pos.append([position[0] + 1, position[1]])

        if self.is_valid([position[0], position[1] - 1]):
            required_pos.append([position[0], position[1] - 1])

        if self.is_safe(position):
            state[0] = 1
        else:
            return state

        #  print("finding in", required_pos)
        for pos in required_pos:
            if self.chart[pos[0]][pos[1]] == -2:
                state[1] = 1
            if self.chart[pos[0]][pos[1]] == -1:
                state[2] = 1

        return state
