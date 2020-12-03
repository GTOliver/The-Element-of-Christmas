
INPUT_FNAME = 'day2input_full.txt'
OUTPUT_FNAME = 'day2input.ele'

beginning = [
    'namespace DayTwoInput',
    '{',
    '    data = list('
]

end = [
    '    )',
    '}'
]

with open(INPUT_FNAME) as fp:
    data = fp.readlines()

data_lines = []
for line in data:
    line = line.strip()
    if line == '':
        continue
    condition, password = [x.strip() for x in line.split(':')]
    allowed_range, key = condition.split(' ')
    lower, upper = allowed_range.split('-')

    keychar_str_as_int = str(ord(key))
    password_as_int_list = 'list(' + ','.join([str(ord(s)) for s in password]) + ')'
    
    indent = ' '*8
    element_line = indent + '{lower=' + lower + ', upper=' + upper + ', key=' + keychar_str_as_int + ', password=' + password_as_int_list + '}'
    data_lines.append(element_line)

beginning_str = '\n'.join(beginning)
data_str = ',\n'.join(data_lines)
end_str = '\n'.join(end)

result = '\n'.join([beginning_str, data_str, end_str])

with open(OUTPUT_FNAME, 'w') as fp:
    fp.write(result)
