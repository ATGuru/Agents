# Example agent template: File Lister
import os

def run():
    print("Files in current directory:")
    for f in os.listdir('.'):
        print(f)

if __name__ == '__main__':
    run()
