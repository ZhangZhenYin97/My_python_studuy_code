'''
计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。（注：字符串末尾不以空格为结尾）
输入一行，代表要计算的字符串，非空，长度小于5000。
输出一个整数，表示输入字符串最后一个单词的长度。
输入：hello nowcoder
输出：8
说明：最后一个单词是nowcode，长度是8
'''


def str_len(str_):
    data_list = str_.split()
    last_word = data_list[-1]
    return len(last_word),last_word


if __name__ == '__main__':
    input_data = input('输入:')
    data,last_word = str_len(input_data)
    # print(f'最后一个单词是{last_word}，长度是{data}')
    print(data)
