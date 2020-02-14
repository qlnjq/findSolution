import copy

class CSPSearchTree:
    def __init__(self):
        print(self, 'does not have an initializer which is fine')


class LV:
    def __init__(self, letter):
        self.letter = letter
        self.value = 0

# def constraints(index, letter):
#         if letter == "A":
#             # print "A = ", index
#             print letter, index
#             loop()
#         elif letter == "B":
#             if index == 3:
#                 return
#             print letter, index
#             loop()


# def loop(initial):
#     # print initial
#     local = list(initial)
#     while len(local) != 0:
#         node = local.pop(0)
#         # local = list(initial)
#
#         for i in range(1, 5):
#             node.value = i
#             if node.letter == "A":
#                 print node.letter, node.value
#                 loop(local)
#             elif node.letter == "B":
#                 if i == 4:
#                     print "B", node.value
#                     return
#                 print "B", node.value
#                 loop(local)


# def constraints(visited):
#     # only cont. if constraints are met
#     if "G" in visited and visited.get("A") < visited.get("G"):
#         # print "A>=G"
#         return 1
#     if "G" in visited and abs(visited.get("G") - visited.get("C")) != 1:
#         # print "|G-C|=1"
#         return 1
#     if "D" in visited and visited.get("D") == visited.get("C"):
#         # print "D!=C" # if D==C, skip
#         return 1
#     if "G" in visited and visited.get("G") == visited.get("F"):
#         # print "G!=F"
#         return 1
#     if "F" in visited and abs(visited.get("E") - visited.get("F")) % 2 == 0:
#         # print "|E-F|=odd"
#         return 1
#     if "H" in visited and visited.get("A") >= visited.get("H"):
#         # print "A<H"
#         return 1
#     if "H" in visited and abs(visited.get("H") - visited.get("C")) % 2 == 1:
#         # print "|H-C| is even"
#         return 1
#     if "E" in visited and visited.get("E") == visited.get("C"):
#         # print "E!=C"
#         return 1
#     if "H" in visited and visited.get("H") == visited.get("F"):
#         # print "H!=F"
#         return 1
#     if "F" in visited and abs(visited.get("F") - visited.get("B")) != 1:
#         # print "|F-B|=1"
#         return 1
#     if "H" in visited and visited.get("H") == visited.get("D"):
#         # print "H!=D"
#         return 1
#     if "E" in visited and visited.get("E") >= (visited.get("D") - 1):
#         # print "E<D-1"
#         return 1
#     if "F" in visited and visited.get("C") == visited.get("F"):
#         # print "C!=F"
#         return 1
#     if "H" in visited and visited.get("G") >= visited.get("H"):
#         # print "G<H"
#         return 1
#     if "G" in visited and visited.get("D") < visited.get("G"):
#         # print "D>=G"
#         return 1
#     if "H" in visited and visited.get("E") == (visited.get("H") - 2):
#         # print "E!=H-2"
#         return 1
#     if "F" in visited and visited.get("D") == visited.get("F"):
#         # print "D!=F"
#         return 1
#     #####
#     # if "C" in visited and visited.get("B") == visited.get("C"):
#     #     print "c!=b", "c = ", visited["C"], "& b = ", visited["B"]
#     #     return 1
#     return 0


def constraints(visited):
    # only cont. if constraints are met
    # 1 == does not meet constraint, so end cycle
    # 0 == pass all constraints and ended at H
    if "D" in visited:
        if visited.get("D") != visited.get("C"):
            pass
        else:
            return 1
    if "E" in visited:
        if visited.get("E") != visited.get("C"):
            pass
        elif visited.get("E") < (visited.get("D") - 1):
            pass
        else:
            return 1
    if "F" in visited:
        if abs(visited.get("E") - visited.get("F")) % 2 == 1:
            pass
        elif abs(visited.get("F") - visited.get("B")) == 1:
            pass
        elif visited.get("C") != visited.get("F"):
            pass
        elif visited.get("D") != visited.get("F"):
            pass
        else:
            return 1
    if "G" in visited:
        if visited.get("A") >= visited.get("G"):
            pass
        elif abs(visited.get("G") - visited.get("C")) == 1:
            pass
        elif visited.get("G") != visited.get("F"):
            pass
        elif visited.get("D") >= visited.get("G"):
            pass
        else:
            return 1
    if "H" in visited:
        if visited.get("A") < visited.get("H"):
            pass
        elif abs(visited.get("H") - visited.get("C")) % 2 == 0:
            pass
        elif visited.get("H") != visited.get("F"):
            pass
        elif visited.get("H") != visited.get("D"):
            pass
        elif visited.get("G") < visited.get("H"):
            pass
        elif visited.get("E") != (visited.get("H") - 2):
            pass
        else:
            return 1
        return 0


def loop(old, values):
    new = list(old)
    if len(new) != 0:
        node = new.pop(0)
        visited = values.copy()
        for i in range(1, 5):
            visited.update({node: i})
            # print visited
            if constraints(visited) == 0:
                print node, i
                loop(new, visited)
            else:
                print node, i, "end"


A = LV("A")
B = LV("B")
C = LV("C")
D = LV("D")
E = LV("E")
F = LV("F")
G = LV("G")
H = LV("H")
# Letters = [A, B, C, D, E, F, G, H]
Letters = ["A", "B", "C", "D", "E", "F", "G", "H"]

# Array = [A, B]
# Letters = ["A", "B", "C", "D"]
loop(Letters, {})

# CSPSearchTree()