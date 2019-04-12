import pyxel

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(0)
    pyxel.circ(80, 60, 20, 8)
    pyxel.circ(80, 60, 15, 9)
    pyxel.circ(80, 60, 10, 10)
    pyxel.circ(80, 60, 5, 0)
    pyxel.blt(66, 90, 0, 0, 0, 16, 16, 0)



pyxel.init(160, 120, caption="Eye of Sauron")
pyxel.load('01_eye_of_sauron.pyxel')
pyxel.run(update, draw)

