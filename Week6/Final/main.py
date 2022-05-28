from raylib import *
import random

InitWindow(1000, 800, b"CYCLE")
SetTargetFPS(60)

class Position:
### initialize positions
    def __init__(self, Lx = 0, Ly = 400, Rx = 990, Ry = 400, Bx = 500, By = 400, scoreL = 0, scoreR = 0):
        self.Lx = Lx
        self.Ly = Ly
        self.Rx = Rx
        self.Ry = Ry
        self.Bx = Bx
        self.By = By
        self.scoreL = scoreL
        self.scoreR = scoreR
    
class Ball:
    ballXspeed = 5
    ballYspeed = [random.randint(-5,5)]

def main():

    def move_left():
        if IsKeyDown(KEY_W):
            P.Ly -= 5 
        if IsKeyDown(KEY_S):
            P.Ly += 5

    def move_right():
        if IsKeyDown(KEY_UP):
            P.Ry -= 5
        if IsKeyDown(KEY_DOWN):
            P.Ry += 5

    P = Position()
    B = Ball()

    moverx = B.ballXspeed
    movery = B.ballYspeed

    movey = movery[-1]

    game_over = False
    while not WindowShouldClose():
        BeginDrawing()
        ClearBackground(WHITE)
        DrawFPS(900, 25)

        while game_over is False:
            BeginDrawing()
            ClearBackground(BLACK)
            DrawFPS(900, 25)

            move_left()
            move_right()

            P.Bx += moverx
            P.By += movey

            if P.Bx == 980 and P.Ry <= P.By <= (P.Ry + 100):
                moverx = -5
                movery.append(random.randint(-5,5))
            if P.Bx == 10 and P.Ly <= P.By <= (P.Ly + 100):
                moverx = 5
                movery.append(random.randint(-5,5))

            if P.By >= 790 or P.By <= 10:
                movey = -movery[-1]
                movery.append(random.randint(-5,5))

            if P.Bx >= 1000:
                P.scoreL += 1
                print(f'Left Score: {P.scoreL}')
                P.Bx -= 500
            if P.Bx <= 0:
                P.scoreR += 1
                print(f'Right Score: {P.scoreR}')
                P.Bx += 500

            if P.scoreL == 5:
                game_over = True
            if P.scoreR == 5:
                game_over = True

            DrawText(f"{P.scoreL} to {P.scoreR}".encode('ascii'), 425, 25, 50, VIOLET)

            DrawRectangle(P.Lx, P.Ly, 10, 100, VIOLET)
            DrawRectangle(P.Rx, P.Ry, 10, 100, VIOLET)
            DrawCircle(P.Bx, P.By, 10, VIOLET)

            EndDrawing()
            
        DrawRectangle(P.Lx, P.Ly, 10, 100, VIOLET)
        DrawRectangle(P.Rx, P.Ry, 10, 100, VIOLET)
        DrawCircle(P.Bx, P.By, 10, VIOLET)
        DrawText("Good Game".encode('ascii'), 250, 300, 100, VIOLET)

        EndDrawing()
    CloseWindow()

main()