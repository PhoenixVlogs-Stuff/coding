import pgzrun
import pgzero
TITLE = "Bouncing ball screensaver"
WIDTH = 700
HEIGHT = 700
GRAVITY = 2000

class Ball:
    def __init__(self, ox,oy,color,radius):
        self.x = ox
        self.y = oy
        self.color = color
        self.vx = 314.1592653589793238462643383279
        self.vy = 3.14159265358979323846264338327950288419716939937510582097494459
        self.radius = radius
    
    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, self.color)

hyperball = Ball(350,350,"#E5FF00",30)
superball = Ball(100,100,"#C55A5A",15)
ball = Ball(500,500,"#00098D",50)
def draw():
    screen.clear()
    hyperball.draw()
    superball.draw()
    ball.draw()

def update(dt):
    #Apply constant acceleration formula
    uy = hyperball.vy
    hyperball.vy += GRAVITY * dt
    hyperball.y += (uy + hyperball.vy) * 0.5 * dt
    if hyperball.y > HEIGHT - hyperball.radius:
        hyperball.y = HEIGHT - hyperball.radius
        hyperball.vy =- hyperball.vy * 0.9
    hyperball.x += hyperball.vx * dt 
    if hyperball.x > WIDTH - hyperball.radius or hyperball.x < hyperball.radius:
        hyperball.vx =- hyperball.vx
    
    uy = ball.vy
    ball.vy += 200 * dt
    ball.y += (uy + ball.vy) * 0.5 * dt
    if ball.y > HEIGHT - ball.radius:
        ball.y = HEIGHT - ball.radius
        ball.vy =- ball.vy * 0.9
    ball.x += ball.vx * dt 
    if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
        ball.vx =- ball.vx

    uy = superball.vy
    superball.vy += 1000 * dt
    superball.y += (uy + superball.vy) * 0.5 * dt
    if superball.y > HEIGHT - superball.radius:
        superball.y = HEIGHT - superball.radius
        superball.vy =- superball.vy * 0.9
    superball.x += superball.vx * dt 
    if superball.x > WIDTH - superball.radius or superball.x < superball.radius:
        superball.vx =- superball.vx

def on_key_down(key):
    if key == keys.Q:
        hyperball.vy = -1000
    if key == keys.A:
        hyperball.vy = +500
    if key == keys.S:
        ball.vy = +1000
    if key == keys.W:
        ball.vy = -200
    if key == keys.D:
        superball.vy = +1000
    if key == keys.E:
        superball.vy = -250
pgzrun.go()