import pyxel

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(12)
    pyxel.rect(20, 0, 29, 49, 7)
    pyxel.rect(0, 20, 49, 29, 7)
    pyxel.rect(50, 10, 159, 19, 7)
    pyxel.rect(50, 30, 159, 39, 7)
    pyxel.rect(0, 50, 159, 59, 7)
    pyxel.rect(0, 70, 159, 79, 7)

pyxel.init(160, 90, caption="Greek Flag")
pyxel.run(update, draw)

