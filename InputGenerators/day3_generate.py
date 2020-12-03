import os 

INPUT_FNAME = 'day3input_full.txt'
OUTPUT_FNAME = 'day3input.ele'

INPUT_DIR = 'input_files'

beginning = [
    'namespace DayThreeInput',
    '{',
    '    data = list('
]

end = [
    '    )',
    '}'
]

with open(os.path.join(INPUT_DIR, INPUT_FNAME)) as fp:
    data = fp.readlines()

data_lines = []
for line in data:
    line = line.strip()
    if line == '':
        continue
    
    list_entries = [str(s == '#') for s in line]

    indent = ' '*8
    data_line = indent + 'list(' + ','.join(list_entries) + ')'
    data_lines.append(data_line)

beginning_str = '\n'.join(beginning)
data_str = ',\n'.join(data_lines)
end_str = '\n'.join(end)

result = '\n'.join([beginning_str, data_str, end_str])

with open(OUTPUT_FNAME, 'w') as fp:
    fp.write(result)
