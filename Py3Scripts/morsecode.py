# 读取文本文件并转为莫尔斯电码，然后使用白色和黑色输出到屏幕。再加上冗余和效验码输出成视频

CODE = {'A': '●▬', 'B': '▬●●●', 'C': '▬●▬●', 'D': '▬●●', 'E': '●',
        'F': '●●▬●', 'G': '▬▬●', 'H': '●●●●', 'I': '●●',
        'J': '●▬▬▬', 'K': '▬●▬', 'L': '●▬●●', 'M': '▬▬', 'N': '▬●',
        'O': '▬▬▬', 'P': '●▬▬●', 'Q': '▬▬●▬', 'R': '●▬●',
        'S': '●●●', 'T': '▬', 'U': '●●▬', 'V': '●●●▬', 'W': '●▬▬',
        'X': '▬●●▬', 'Y': '▬●▬▬', 'Z': '▬▬●●',

        '0': '▬▬▬▬▬', '1': '●▬▬▬▬', '2': '●●▬▬▬', '3': '●●●▬▬',
        '4': '●●●●▬', '5': '●●●●●', '6': '▬●●●●', '7': '▬▬●●●',
        '8': '▬▬▬●●', '9': '▬▬▬▬●',

        '.': '●▬●▬●▬', ',': '▬▬●●▬▬', ':': '▬▬▬●●●',
        '?': '●●▬▬●●', '\'': '●▬▬▬▬●', '-': '▬●●●●▬',
        '/': '▬●●▬●', '@': '●▬▬●▬●', '=': '▬●●●▬', ' ': '/'
        }

CODE_REVERSED = {value: key for key, value in CODE.items()}


def to_morse(s):
    return ' '.join(CODE.get(i.upper()) for i in s)


def from_morse(s):
    return ''.join(CODE_REVERSED.get(i) for i in s.split())


morse = to_morse('living')
space = to_morse(' ')
text = from_morse('▬▬●●▬▬')
print(morse)
print(text)