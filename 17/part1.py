def do_step(x, y, vx, vy):
    x += vx
    y += vy
    if vx != 0:
        vx -= vx/abs(vx)
    vy -= 1
    return x, y, vx, vy


def simulate(vx, vy, target_x, target_y):
    x, y = 0, 0
    heights = []
    while True:
        x, y, vx, vy = do_step(x, y, vx, vy)
        heights.append(y)
        if x in target_x and y in target_y:
            return True, max(heights)
        if x > max(target_x) or y < min(target_y):
            return False, max(heights)


target_x = range(143, 178)
target_y = range(-106, -70)
total_max_y = -float('inf')
for vx in range(1, 100):
    for vy in range(-100, 200):
        result, max_y = simulate(vx, vy, target_x, target_y)
        if result and max_y > total_max_y:
            total_max_y = max_y

print(total_max_y)
