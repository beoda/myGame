#
import random
import time

def main():
    lines = [0,1,2,3,4,5,6]
    colums = [0,1,2,3,4,5,6]

    # make game infinite
    game = 1

    #initial position
    player = [0,3]

    #initial position of obstacles
    obstacles = [[5, 1], [3, 4], [6, 2], [0, 4], [2, 3], [1, 6], [4, 6]]

    #game speed
    SPEED = 2

    #score of player
    SCORE = 0

    while game <= 1:
        for i in range(0,6,1):
            for j in range(0,6,1):
                time.sleep(SPEED)
                obstacles = [i,j]
                print(obstacles)
                x = random.randint(0,7)
                player = [0,x]
                # collision condition
                if(obstacles == player):
                    print("Game Over")
                else:
                    print("Game in progress")
                    SCORE = SCORE + 10
                    print("your score is", SCORE)
                    if (SCORE % 50 == 0):
                        SPEED = SPEED/10
if __name__ == '__main__':
    main()