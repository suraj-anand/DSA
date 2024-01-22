def compareVersions(version1: str, version2: str):
    
    version1_list = list(reversed(version1.split(".")))
    version2_list = list(reversed(version2.split(".")))
    
    val_version1, val_version2 = 0, 0
    factor = 1
    print(version1_list, version2_list)
    for index, val in enumerate(version1_list):
        val_version1 = (val_version1 * factor) + int(val) 
        factor *= 10
    
    factor = 1
    for index, val in enumerate(version2_list):
        val_version2 = (val_version2 * factor) + int(val) 
        factor *= 10
        
    print(val_version1)
    print(val_version2)
    
    if val_version1 > val_version2:
        return -1
    elif val_version1 < val_version2:
        return 1
    else:
        return 0

version1 = "0.1"
version2 = "0.1.0"

result = compareVersions(version1, version2)