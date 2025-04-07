if __name__ == "__main__":
    '''File that sums up the arguments decoded. '''
    import sys
    total = 0
    for i in range(len(sys.argv) -1):
        total += int(sys.argv[i + 1])
        print(total)

        


          