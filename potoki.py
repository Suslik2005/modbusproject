import threading

c1 = 0
c2 = 0
def greet(be,cam):
    global c1
    global c2
    while True:
        if cam == "c1":
            c1+=1
            print(f'num {cam}: {c1} ;')
        else:
            c2+=1
            print(f'num {cam}: {c2} ;')



if __name__ == '__main__':
    t1 = threading.Thread(target=greet, args=(c1, 'c1',), daemon=True)
    t2 = threading.Thread(target=greet, args=(c2, 'c2',), daemon=True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()