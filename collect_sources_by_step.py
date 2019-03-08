import numpy as np
import pandas as pd


def to_numstr(n):
    """
    `n`을 문자형으로 바꾸고 한 자리 수면 앞에 0을 붙인다.
    """
    n = str(n)
    if len(n) == 1:
        n = '0' + n
    return n


# 소스코드가 있는 디렉토리
src_dir = 'archive'
# 단계별 풀이가 저장될 디렉토리
out_dir = 'step_solution'

step_df = pd.read_csv('step.csv')
steps = np.unique(step_df.step.values)

for s in steps:
    path = out_dir + '/step_' + to_numstr(s) + '.md'
    outfile = open(path, 'w')
    
    # `s` 단계에 해당하는 문제 번호들
    probs = step_df.problem[step_df.step == s].values
    # 해당 소스 파일들
    files = ['prob_' + str(n) for n in probs]
    
    for i, f in enumerate(files):
        # i번째 문제 제목을 쓴다.
        outfile.write('## ' + str(i + 1) + '. ' + f + '\n\n')
        path = src_dir + '/' + f + '.py'
        # 코드 블록을 만들고 문제 풀이 소스를 쓴다.
        try:
            src = open(path, 'r').read()
            outfile.write('```python\n')
            outfile.write(src)
            outfile.write('```\n\n')
        # 해당 소스 파일이 없으면 'None'을 쓴다.
        except FileNotFoundError:
            outfile.write('None\n\n')
    
    outfile.close()
