import os 

INPUT_FNAME = 'day8input_example.txt'
OUTPUT_FNAME = 'day8input.ele'

INPUT_DIR = 'input_files'

BEGINNING = [
    'namespace DayEightInput',
    '{',
    '    data = list('
]

END = [
    '    )',
    '}'
]

def main():
    with open(os.path.join(INPUT_DIR, INPUT_FNAME)) as fp:
        data = fp.readlines()

    data_lines = []
    for line in data:
        line = line.strip()
        if line == '':
            continue
        
        instruction, value = line.split(' ')

        element_chars = ['Char.'+c for c in instruction]
        element_string_struct = 'String(list(' + ', '.join(element_chars) + '))'

        element_anonymous_block = '{operation=' + element_string_struct + ', argument=' + str(int(value)) + '}'
        
        indent = ' '*8
        data_line = indent + element_anonymous_block
        data_lines.append(data_line)

    beginning_str = '\n'.join(BEGINNING)
    data_str = ',\n'.join(data_lines)
    end_str = '\n'.join(END)

    result = '\n'.join([beginning_str, data_str, end_str])

    with open(OUTPUT_FNAME, 'w') as fp:
        fp.write(result)

if __name__ == '__main__':
    main()
