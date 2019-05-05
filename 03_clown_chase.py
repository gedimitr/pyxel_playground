import pyxel

koritsi_dx = 0
koritsi_dy = 0
koritsi_x = 50
koritsi_y = 50
koritsi_tsirizi=False

clown_dx = 0
clown_dy = 0
clown_x = 100
clown_y = 50



def update():
    global koritsi_dx, koritsi_dy, clown_dx, clown_dy, koritsi_tsirizi

    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    if pyxel.btnp(pyxel.KEY_LEFT):
        koritsi_dx = -1
    if pyxel.btnp(pyxel.KEY_RIGHT):
        koritsi_dx = 1
    if pyxel.btnr(pyxel.KEY_LEFT) or pyxel.btnr(pyxel.KEY_RIGHT):
        koritsi_dx = 0
    if pyxel.btnp(pyxel.KEY_UP):
        koritsi_dy = -1
    if pyxel.btnp(pyxel.KEY_DOWN):
        koritsi_dy = 1
    if pyxel.btnr(pyxel.KEY_UP) or pyxel.btnr(pyxel.KEY_DOWN):
        koritsi_dy = 0

    if pyxel.btnp(pyxel.KEY_A):
        clown_dx = -1
    if pyxel.btnp(pyxel.KEY_D):
        clown_dx = 1
    if pyxel.btnr(pyxel.KEY_A) or pyxel.btnr(pyxel.KEY_D):
        clown_dx = 0
    if pyxel.btnp(pyxel.KEY_W):
        clown_dy = -1
    if pyxel.btnp   (pyxel.KEY_S):
        clown_dy = 1
    if pyxel.btnr(pyxel.KEY_W) or pyxel.btnr(pyxel.KEY_S):
        clown_dy = 0

    if pyxel.btnp(pyxel.KEY_CONTROL):
        koritsi_tsirizi=True
        pyxel.playm(0, loop=True)

    if pyxel.btnr(pyxel.KEY_CONTROL):
        koritsi_tsirizi=False
        pyxel.stop()
        


def draw():
    global koritsi_x, koritsi_y, clown_x, clown_y

    pyxel.cls(0)
    koritsi_x = koritsi_x + koritsi_dx
    koritsi_y = koritsi_y + koritsi_dy
    pyxel.blt(koritsi_x, koritsi_y, 0, 0, 0, 16, 16)
    if koritsi_tsirizi:
        pyxel.blt(koritsi_x+10, koritsi_y+2, 0, 32, 0, 8, 8, 0)

    clown_x = clown_x + clown_dx
    clown_y = clown_y + clown_dy
    pyxel.blt(clown_x, clown_y, 0, 18, 0, 12, 16, 0)

pyxel.init(160, 120, caption="Clown Chase")
pyxel.load('03_clown_chase.pyxel')
pyxel.run(update, draw)

