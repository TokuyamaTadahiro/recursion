import sys
import markdown

def markdown_def(input_path,output_path):
    with open(input_path,'r') as f:
        contents = f.read()

    html = markdown.markdown(contents)
    with open(output_path,'w') as f:
        f.write(html)
        print("converted.")

def main():
    if len(sys.argv) < 4:
        print("入力を確認してください。")
        return
    
    option = sys.argv[1]
    input_path = sys.argv[2]
    output_path = sys.argv[3]

    if option == 'markdown':
        markdown_def(input_path,output_path)
    else:
        print("optionを確認してください。")
        return

if __name__ == "__main__":
    main()
