import os

clearConsole=lambda:os.system('cls')

def checkType():
    print('Give data:\n')
    data=input()
    try:
        int(data);
        print ("Integer number",end='')
    except ValueError:
        try:
            float(data)
            print ("Float number",end='')
        except ValueError:
            try:
                str(data)
                print ("string data",end='')
            except:
                print ("something different",end='')
    finally:
        print("\nEnd Program \nTo end program press button",end='')
        input()


def main():
    clearConsole()
    checkType()

main()