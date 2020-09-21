import csv
import os, sys

def main():
    input_filepath  = input('表を生成するCSVファイルのパスを指定してください．\n>> ')
    output_filepath = input('表のソースを出力するファイルのパスを指定してください．\n>>')

    # CSVファイルを読み込む
    if os.path.isfile(input_filepath):
        with open(input_filepath, 'r') as inputed_file:
            records = list(csv.reader(inputed_file))

        output_source = str()
        for record in records:
            for idx, value in enumerate(record):
                if value == '':
                    if idx == 0:
                        output_source += 'None'
                    else:
                        output_source += '&None'
                else:
                    if idx == 0:
                        output_source += value
                    else:
                        output_source += '&' + value

            output_source += " \\\\ \hline\n"

        with open(output_filepath, 'w') as output_file:
            output_file.write(output_source)

if __name__ == '__main__':
    main()
