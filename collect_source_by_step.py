src_dir = 'archive'

# step 01
outfile = open('step_01.md', 'w')
step_01 = [2557, 1000, 1001, 7287, 10172, 10718, 11718, 11719]
files = ['prob_' + str(num) for num in step_01]
for i, f in enumerate(files):
    outfile.write('## ' + str(i + 1) + '. ' + f + '\n\n')
    path = src_dir + '/' + f + '.py'
    try:
        src = open(path, 'r').read()
        outfile.write('```python\n')
        outfile.write(src)
        outfile.write('```\n\n')
    except FileNotFoundError:
        outfile.write('None\n\n')
outfile.close()
