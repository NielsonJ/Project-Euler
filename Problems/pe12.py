import time

def main():
    print('script started ...')
    start = time.clock()
    answer = 0
    end = time.clock()
    print('answer: ' + str(answer))
    print('time: ' + str(end - start))

if __name__ == '__main__':
    main()