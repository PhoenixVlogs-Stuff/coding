import pgzrun
import pgzero
TITLE = "Bouncing ball screensaver"
WIDTH = 700
HEIGHT = 700
GRAVITY = 2000

class Ball:
    def __init__(self, ox,oy):
        self.x = ox
        self.y = oy
        self.vx = 314.1592653589793238462643383279
        self.vy = 3.14159265358979323846264338327950288419716939937510582097494459
        self.radius = 31.41592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844
    
    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, "#C2CC00")

hyperball = Ball(350,350)
def draw():
    screen.clear()
    hyperball.draw()

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

def on_key_down(key):
    if key == keys.SPACE:
        hyperball.vy = -510
    if key == keys.S:
        hyperball.vy = +500
pgzrun.go()