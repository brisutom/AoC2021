import operator


def hex2bin(h):
    return bin(int(h, 16))[2:].zfill(len(h) * 4)


def parse_packet(packet, start):
    val = None
    i = start
    version = int(packet[i:i+3], 2)
    type_id = int(packet[i+3:i+6], 2)
    if type_id == 4:
        # literal
        literal_value = []
        i += 6
        do_next = True
        while do_next:
            if packet[i] == "0":
                do_next = False
            literal_value.append(packet[i+1:i+5])
            i += 5
        val = int("".join(literal_value), 2)
    else:
        # operator
        i += 6
        if packet[i] == "0":
            sub_len = int(packet[i+1:i+16], 2)
            i += 16
            curr_len = 0
            while curr_len < sub_len:
                sub_i, sub_ver, sub_val = parse_packet(packet, i)
                i += sub_i
                curr_len += sub_i
                version += sub_ver
                val = do_operations(type_id, sub_val, val)
        elif packet[i] == "1":
            sub_num = int(packet[i+1:i+12], 2)
            i += 12
            for _ in range(sub_num):
                sub_i, sub_ver, sub_val = parse_packet(packet, i)
                i += sub_i
                version += sub_ver
                val = do_operations(type_id, sub_val, val)
    bits_parsed = i - start
    return bits_parsed, version, val


def do_operations(type_id, second, first):
    if first is None:
        return second
    operations = [operator.add, operator.mul, min, max, operator.lt,
                  operator.gt, operator.eq]
    operations = dict(zip([0, 1, 2, 3, 5, 6, 7], operations))
    result = operations[type_id](second, first)
    return int(result)


packet = open("input.txt").readline()
packet = hex2bin(packet)
_, _, value = parse_packet(packet, 0)
print(value)
