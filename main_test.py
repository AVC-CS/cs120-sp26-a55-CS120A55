import pytest
import re

def regex_test(expected, content):
    pos = 0
    for token in expected:
        res = re.search(token, content[pos:])
        if res is None:
            assert False, f'Expect: {token}'
        pos += res.start() + 1

@pytest.mark.T1
def test_main_1():
    # 2 students, 3 scores each: Alice 80 90 100 -> total=270 avg=90; Bob 60 70 80 -> total=210 avg=70
    content = open('result1.txt').read()
    print(content)
    regex_test([r'Alice.*270.*90', r'Bob.*210.*70'], content)

@pytest.mark.T2
def test_main_2():
    # 3 students, 2 scores each: James 90 100 -> 190 avg=95; Michael 90 90 -> 180 avg=90
    content = open('result2.txt').read()
    print(content)
    regex_test([r'James.*190.*95', r'Michael.*180.*90'], content)

@pytest.mark.T3
def test_main_3():
    # 1 student, 4 scores: Sara 25 25 25 25 -> total=100 avg=25
    content = open('result3.txt').read()
    print(content)
    regex_test([r'Sara.*100.*25'], content)

@pytest.mark.T4
def test_main_4():
    # 4 students, 2 scores: James 90 100 -> 190 avg=95; Linda 100 100 -> 200 avg=100
    content = open('result4.txt').read()
    print(content)
    regex_test([r'James.*190.*95', r'Linda.*200.*100'], content)
