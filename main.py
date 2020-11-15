import codecs, markdown

# 读取 markdown 文本
input_file = codecs.open("article/0000-CentOS环境准备.md", mode="r", encoding="utf-8")
text = input_file.read()

# 转为 html 文本
html = markdown.markdown(text)
html='''
<meta charset='UTF-8'><meta name='viewport' content='width=device-width initial-scale=1'>
'''+html
# 保存为文件
output_file = codecs.open("page/0000-CentOS环境准备-2.html", mode="w", encoding="utf-8")
output_file.write(html)