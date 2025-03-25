import time

def liftoff():
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)
    print("🚀 Liftoff!")

if __name__ == "__main__":
    liftoff()
