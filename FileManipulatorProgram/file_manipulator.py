import sys
import re

def reverse(input_path,output_path):
    with open(input_path, 'r') as f:
        contents = f.read()
    
    reversed_s = contents[::-1]

    with open(output_path, 'w') as f:
        f.write(reversed_s)
        print('reverse Done.')

def copy(input_path,output_path):
    with open(input_path, 'r') as f:
        contents = f.read()

    with open(output_path,'w') as f:
        f.write(contents)
        print('Copy Done.')


def duplicate_contents(input_path,n):
    with open(input_path,'r') as f:
        contents = f.read()
    
    save = contents
    while n > 1:
        contents += save
        n -= 1

    with open(input_path, 'w') as f:
        f.write(contents)
        print("duplicate-contents Done.")

def duplicate_contents_Helper(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def replace_string(input_path,old_string,new_string):
    with open(input_path,'r') as f:
        contents = f.read()

    new_contents = re.sub(old_string,new_string,contents)

    with open(input_path,'w') as f:
        f.write(new_contents)
        print("replace-string Done.")

def main():
    if len(sys.argv) < 4:
        print("引数かパスが足りません\n")
        return
    
    option = sys.argv[1]
    input_path = sys.argv[2]
    output_path = sys.argv[3]

    if option == 'reverse':
        reverse(input_path,output_path)
    elif option == 'copy':
        copy(input_path,output_path)
    elif option == 'duplicate-contents':
        if(duplicate_contents_Helper(sys.argv[3])):
            duplicate_contents(input_path,int(sys.argv[3]))
        else:
            print("入力値のエラーがあります。\n")
            return
    elif option == 'replace-string':
        if len(sys.argv) != 5:
            print("入力をチェックしてください。\n")
            return
        old_string = sys.argv[3]
        new_string = sys.argv[4]
        replace_string(input_path,old_string,new_string)

if __name__ == "__main__":
    main()

