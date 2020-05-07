import re
re.search(r'FishC', 'I love FishC.com!')
#.号可以匹配所有字符
re.search(r'Fis.', 'I love FishC.com!')
"""
如果想单独搜索.号可以在前面加上反斜杠\
\d匹配任何数字
创建一个字符类，用中括号创建一个字符类，只要匹配字符类内的任何一个字符就都算匹配
默认是有大小写模式的
"""
re.search(r'[aeiou]','I love xiaotang!')
#可以用小横杠来表示范围
re.search(r'[a-z]','I love xiaotang!')
re.search(r'[0-9]','I love xiaotang!')
re.search(r'[2-9]','I love xiaotang!')
#限定重复匹配的次数可以用大括号解决
re.search(r'ab{3}c','abbbc')
re.search(r'ab{3}c','abbbbbbbbc')#no只能是3次
#也可以让b在一个重复的范围中,用逗号就可以了
re.search(r'ab{3,10}c','abbbbbbbbc')
#正则表达式匹配的字符串，匹配数字只能一个
#匹配数字的255以内
re.search(r'1\d\d|2[0-4]\d|25[0-5]|\d\d|\d','8')
#匹配一个IP地址的话,01是可以选的，所以设置重复的次数，0次就是没有，或者1次 
re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])','192.168.1.1')
