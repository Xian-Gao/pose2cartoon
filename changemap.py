def ChangeMap(filename):
    filedata = ""
    f = open(filename, "r")
    for line in f:
        if line.split()[0] == 'map_Kd':
            line = line.replace(line, "map_Kd " + line.split()[1].split('\\')[-1] + "\n")
        # print(line)
        filedata += line

    f = open(filename, "w")
    f.write(filedata)


ChangeMap("sources/test_module/Butcher_intermediate1.mtl")
