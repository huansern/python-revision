from sty import fg

def swap(data, x, y, visible = True, color = 201):
    data[x], data[y] = data[y], data[x]

    if not visible or x == y:
        return
    if x > y:
        x, y = y, x
    print(
        *data[:x],
        fg(color) + str(data[x]) + fg.rs,
        *data[x + 1:y],
        fg(color) + str(data[y]) + fg.rs,
        *data[y + 1:]
    )
