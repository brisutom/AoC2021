def do_step(x, y, vx, vy):
    x += vx
    y += vy
    if vx != 0:
        vx -= vx/abs(vx)
    vy -= 1
    return x, y, vx, vy


def simulate(vx, vy, target_x, target_y):
    x, y = 0, 0
    while True:
        x, y, vx, vy = do_step(x, y, vx, vy)
        if x in target_x and y in target_y:
            return True
        if x > max(target_x) or y < min(target_y):
            return False


target_x = range(143, 178)
target_y = range(-106, -70)
success = []
for vx in range(1, 1000):
    for vy in range(-200, 200):
        result = simulate(vx, vy, target_x, target_y)
        success.append(result)

print(success.count(True))
