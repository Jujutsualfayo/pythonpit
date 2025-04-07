if __name__ == "__main__":
    '''File to add sum of arguments.'''
    
    import sys
    total = 0
    for i in range(len(sys.argv) -1):
        total += int(sys.argv[i + 1])
        print(total)
        


          