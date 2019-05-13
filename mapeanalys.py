def calculateError(CSVFile: object):
    errorTab = []
    for i in range(0, len(CSVFile)):
        errorTab.append(CSVFile.get_values())