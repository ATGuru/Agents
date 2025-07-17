import time

# Task Reminder Agent
def run():
    print('Task reminder running...')
    while True:
        print('Reminder: Check your tasks!')
        time.sleep(3600)

if __name__ == '__main__':
    run()
