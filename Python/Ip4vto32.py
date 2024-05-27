"""
Params
"""
def ip_to_int32(ip: str)->int:
    ##
    splitIp = ip.split(".")
    newSplitIp = list(map(int, splitIp))
    binaryArray = [format(x, '08b') for x in newSplitIp]
    binaryStr = "".join(binaryArray)
    result = int(binaryStr, 2)
    return result

def main():
    currentIPAddr = "128.32.10.1"
    print(ip_to_int32(currentIPAddr))


if __name__ in "__main__":
    main()