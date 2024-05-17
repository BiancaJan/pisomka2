import tkinter as tk

def klikaj(event):
    global z_r, z_s
    r = event.y // strana
    s = event.x // strana
    if z_r == -1:
        z_r, z_s == r,s
        canvas.itemconfig(siet[r][s], fill="blue")
    else:
        if z_r == r:
            for i in range(min(s,z_s),max(s,z_s)+1):
                canvas.itemconfig(siet[r][i],fill="blue")
        elif z_s == s:
            for i in range(min(r,z_r),max(r,z_r) + 1):
                canvas.itemconfig(siet[i][s],fill = "blue")
        else:
            canvas.itemconfig(siet[z_r][z_s],fill = "white" )
        z_r,z_s = -1, -1

strana = 40
sirka = 10
vyska = 10
canvas = tk.Canvas(width=sirka*strana,height=vyska*strana, bg="white")
siet = []
for r in range(vyska):
    riadok = []
    for s in range(sirka):
        riadok.append(canvas.create_rectangle(s*strana, r*strana, (s+1)*strana, (r+1)*strana, fill='white'))
    siet.append(riadok)
canvas.pack()
z_r, z_s = -1, -1
canvas.bind("<Button-1>", klikaj)

canvas.mainloop()

