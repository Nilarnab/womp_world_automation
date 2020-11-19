from game import game

class Agent:
    def __init__(self):
        """
        The knowledge base actually gives the map that is made in the mind of the agent
        in addition to this
        there is safe array, giving the position of all the safe array
        there is visited array, giving the list of visited array
        """
        print("Starting quest")
        print("I am at 0 0")

        self.knowledge_base = [[None for i in range(4)] for i in range(4)]

        for i in range(len(self.knowledge_base)):
            for j in range(len(self.knowledge_base[i])):
                print([self.knowledge_base[i][j]], end=" ")
            print("")

        # the place where the agent is standing is safe
        # making 0, 0 safe
        self.safe = [[0, 0]]
        # making a list for visited areas
        self.visited = []


def play_game(position):
    """
    This is the main function that is responsible for the progress of the game

    intiution
    1. Find if alive
    2. Find the possible next approaches
    3. if it is not stenching or breezing all moves are safe
    4. if it is stenching or breeing in any possible approaches,
        then find in the knowledge base if any other adjecent place is also stechning or breezing
        if the other is not stenching, then it is definitely safe

        otherwise no step is possible
    5. add all the newly found safe approaches in the KB
    6. add the current place as visited
    7. play the game for all the safe but not visited places


    :param position: [xth row, yth column]
    :return: None
    """

    print("position", position)
    print("my current knowledge base is ", agent.knowledge_base)

    # getting data from sensors
    state = game.get_state(position)

    # inserting data into knowledge base
    agent.knowledge_base[position[0]][position[1]] = state
    # adding data of visited and safe positions in knowledge base
    if position not in agent.visited:
        agent.visited.append(position)
    if position not in agent.safe:
        agent.safe.append(position)

    if not stench_feel:
        # if the womp is down, there is no stench
        state[1] = 0
    print("present state", state)
    if game.is_successful(position):
        print("Successful")
        visited = agent.visited
        visited.sort()

        print(5*"\n")
        print("shortest path")
        cur = [0, 0]
        print(cur, end=" ")
        for pos in visited[1: ]:
            if cur[0] <= pos[0] and cur[1] <= pos[1]:
                print("->", pos,  end=" ")
                cur = pos
        exit()

    if game.is_safe(position):
        # alive
        poss_approaches = []
        if game.is_valid([position[0] + 1, position[1]]):
            poss_approaches.append([position[0] + 1, position[1]])

        if game.is_valid([position[0] - 1, position[1]]):
            poss_approaches.append([position[0] - 1, position[1]])

        if game.is_valid([position[0], position[1] - 1]):
            poss_approaches.append([position[0], position[1] - 1])

        if game.is_valid([position[0], position[1] + 1]):
            poss_approaches.append([position[0], position[1] + 1])

        # print("Possible approaches", poss_approaches)

        # finding safe approaches
        safe_next_approach = []
        if state[1] == state[2] == 0:
            # not stenching or breezing
            # so all the next approaches are safe
            safe_next_approach = poss_approaches
        else:
            # one of the next approaches are unsafe
            # only those steps will be chosen which are for sure safe
            # by using the data of knowledge base and the rules of the game
            for pos in poss_approaches:
                surr_pos = []
                # intuition behind this step
                # if a step is safe
                # for example
                # [1, 0] for
                # the next step [1, 1] is safe as
                # if there is the monster in [1, 1] there should be stench in both
                # [1, 0] and [0, 1]
                # void   stench
                # breeze ??????

                # if the knowledge is not sufficient to give such data
                # the approach is skipped by considering risky




                if game.is_valid([pos[0] + 1, pos[1]]):
                    surr_pos.append([pos[0] + 1, pos[1]])

                if game.is_valid([pos[0] - 1, pos[1]]):
                    surr_pos.append([pos[0] - 1, pos[1]])

                if game.is_valid([pos[0], pos[1] - 1]):
                    surr_pos.append([pos[0], pos[1] - 1])

                if game.is_valid([pos[0], pos[1] + 1]):
                    surr_pos.append([pos[0], pos[1] + 1])

                # print("surrounding of", pos, "is found as", surr_pos)
                for new_pos in surr_pos:
                    # print("new pos", new_pos)
                    new_state = agent.knowledge_base[new_pos[0]][new_pos[1]]
                    # print("new state", new_state)
                    if new_state is not None:
                        # i have data about this place
                        if state[1] == 1 and state[2] == 0:
                            if (new_state[1] != state[1]) and new_pos != pos:
                                # if game.is_safe(pos):
                                # the next place is safe!!!
                                safe_next_approach.append(pos)
                                break

                        if state[2] == 1 and state[1] == 0:
                            if (new_state[2] != state[2]) and new_pos != pos:
                                # if game.is_safe(pos):
                                # the next place is safe!!!
                                safe_next_approach.append(pos)
                                break

                        if state[1] == 1 and state[2] == 1:
                            if (new_state[1] != state[1] and new_state[2] != state[2]) and new_pos != pos:
                                # if game.is_safe(pos):
                                # the next place is safe!!!
                                safe_next_approach.append(pos)
                                break

        print("safe_next positinos", safe_next_approach)
        for safe_pos in safe_next_approach:
            agent.safe.append(safe_pos)
        # recursing for all the safe optoins

        for safe_pos in safe_next_approach:
            if safe_pos not in agent.visited:
                play_game(safe_pos)

    else:
        print("DEATH!")
        exit()


rows = 4
columns = 4
game = game.World()
print("")
success = False
retry = True
stench_feel = True
agent = Agent()
play_game([0, 0])

if not success and retry:
    retry = False
    print("Shooting the arrow")
    stench_feel = False
    play_game([0, 0])

