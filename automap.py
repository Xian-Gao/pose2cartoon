'''
Automatically map joints in .txt file to smpl joints.
Usage: manual_model_to_smpl = AutoMap(filename)
'''

def AutoMap(infoname):
  '''
  Firstly, we get the joint indices in .txt file.
  '''
    lines = open(infoname, encoding='utf-8').readlines()
    hier = {}
    joint2index = {}
    index = 0
    for line in lines:
        line = line.strip('\n').strip()
        if line[:4] != 'hier':
            continue
        splits = line.split(' ')
        parent_name = splits[1]
        child_name = splits[2]
        if parent_name not in joint2index:
            joint2index[parent_name] = index
            index += 1
        if child_name not in joint2index:
            joint2index[child_name] = index
            index += 1
        if parent_name not in hier:
            hier[parent_name] = [child_name]
        else:
            hier[parent_name].append(child_name)

    index2joint = {v: k for k, v in joint2index.items()}
    hier_index = {}
    for k, v in hier.items():
        hier_index[joint2index[k]] = [joint2index[vv] for vv in v]
    parents = list(hier_index.keys())
    children = []
    for v in hier_index.values():
        children.extend(v)
    root = [item for item in parents if item not in children]
    assert len(root) == 1
    root = root[0]

    new_joint2index = {index2joint[root]: 0}
    top_level = [root]
    index = 1
    for item in top_level:
        if item not in hier_index:
            continue
        for child in hier_index[item]:
            child_name = index2joint[child]
            if child_name not in new_joint2index:
                new_joint2index[child_name] = index
                index += 1
            top_level.append(child)

    '''
    Now we have the dictionary new_joint2index storing joint names and indices.
    Then we map them.
                
                ……
                index += 1
            top_level.append(child)
            ---Cont'd---
    '''

    map_sequence = str(new_joint2index)[1:-1].split(',')

    smpl = "{"
    for i in range(len(map_sequence)):
        line = map_sequence[i].replace("'", "").split(':')[-2] \
               + ":" + map_sequence[i].replace("'", "").split(':')[-1]
        key = key.replace("R","right")
        key = key.replace("L","left")
        key = line.split(":")[-2].lower().replace(" ", "")
        key = key.replace("thigh","upleg")
        key = key.replace("elbow","shoulder")
        key = key.replace("calf","leg")
        key = key.replace("ankle","foot")
        key = key.replace("collar","shoulder")
        key = key.replace("upperarm","arm")
        # print(key)

        if key == "hips":  # 0
            smpl += (str(i) + ":0,")
        elif key == "leftupleg":  # 1
            smpl += (str(i) + ":1,")
        elif key == "rightupleg":  # 2
            smpl += (str(i) + ":2,")
        elif key == 'spine':  # 3
            smpl += (str(i) + ":3,")
        elif key == "leftleg":  # 4
            smpl += (str(i) + ":4,")
        elif key == "rightleg":  # 5
            smpl += (str(i) + ":5,")
        elif key == "spine1":  # 6
            smpl += (str(i) + ":6,")
        elif key == "leftfoot":  # 7
            smpl += (str(i) + ":7,")
        elif key == "rightfoot":  # 8
            smpl += (str(i) + ":8,")
        elif key == "spine2":  # 9
            smpl += (str(i) + ":9,")
        elif key == "lefttoebase":  # 10
            smpl += (str(i) + ":10,")
        elif key == "righttoebase":  # 11
            smpl += (str(i) + ":11,")
        elif key == "neck":  # 12
            smpl += (str(i) + ":12,")
        elif key == "leftshoulder":  # 13
            smpl += (str(i) + ":13,")
        elif key == "rightshoulder":  # 14
            smpl += (str(i) + ":14,")
        elif key == "head":  # 15
            smpl += (str(i) + ":15,")
        elif key == "leftarm":  # 16
            smpl += (str(i) + ":16,")
        elif key == "rightarm":  # 17
            smpl += (str(i) + ":17,")
        elif key == "leftforearm":  # 18
            smpl += (str(i) + ":18,")
        elif key == "rightforearm":  # 19
            smpl += (str(i) + ":19,")
        elif key == "lefthand":  # 20
            smpl += (str(i) + ":20,")
        elif key == "righthand":  # 21
            smpl += (str(i) + ":21,")
        elif key == "lefthandindex1":  # 22
            smpl += (str(i) + ":22,")
        elif key == "righthandindex1":  # 23
            smpl += (str(i) + ":23,")
        else:
            continue
    smpl += "}"

    smpl = eval(smpl)
    # print(smpl)
    return smpl


AutoMap("sources/test_module/Butcher.txt")
