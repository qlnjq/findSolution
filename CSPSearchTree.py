def constraints(curr, visited):
    # only cont. if constraints are met
    # 1 == does not meet constraint, so end cycle
    # 0 == pass all constraints
    # 2 == pass all constraints and ended at H
    if "D" == curr:
        if not visited.get("D") != visited.get("C"):
            return 1
    if "E" == curr:
        if not visited.get("E") != visited.get("C"):
            return 1
        if not visited.get("E") < (visited.get("D") - 1):
            return 1
    if "F" == curr:
        if not abs(visited.get("E") - visited.get("F")) % 2 == 1:
            return 1
        if not abs(visited.get("F") - visited.get("B")) == 1:
            return 1
        if not visited.get("C") != visited.get("F"):
            return 1
        if not visited.get("D") != visited.get("F"):
            return 1
    if "G" == curr:
        if not visited.get("A") >= visited.get("G"):
            return 1
        if not abs(visited.get("G") - visited.get("C")) == 1:
            return 1
        if not visited.get("G") != visited.get("F"):
            return 1
        if not visited.get("D") >= visited.get("G"):
            return 1
    if "H" == curr:
        if not visited.get("A") < visited.get("H"):
            return 1
        if not abs(visited.get("H") - visited.get("C")) % 2 == 0:
            return 1
        if not visited.get("H") != visited.get("F"):
            return 1
        if not visited.get("H") != visited.get("D"):
            return 1
        if not visited.get("G") < visited.get("H"):
            return 1
        if not visited.get("E") != (visited.get("H") - 2):
            return 1
        return 2
    return 0


def loop(old, values, count):
    # count[success, fail]
    new = list(old)
    if len(new) != 0:
        node = new.pop(0)
        visited = values.copy()
        for i in range(1, 5):
            visited.update({node: i})
            # print visited
            result = constraints(node, visited)
            if result == 0:
                print node, i
                loop(new, visited, count)
            elif result == 2:
                count[0] += 1
                print "reached, count = ", count
            else:
                count[1] += 1
                print node, i


Letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
count = [0, 0]
loop(Letters, {}, count)
print "success = ", count[0], "; fail =", count[1]
