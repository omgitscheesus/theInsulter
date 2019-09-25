def getInsults_file(file_location):
    insult_list = []
    with open(file_location) as file:
        for line in file:
            insult_list.append(line)
    return insult_list
