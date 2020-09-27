#!/usr/bin/python3
def canUnlockAll(boxes):
    """Unlock the Boxes project """
    check_list = [False] * len(boxes)
    check_list[0] = True
    for i in range(0, len(boxes)):
        if isinstance(boxes[i], list):
            for j in range(len(boxes[i])):
                if boxes[i][j] <= len(boxes) and boxes[i][j] != i:
                    check_list[boxes[i][j]] = True
    if False in check_list:
        return False
    else:
        return True
