import codecs, markdown
import os

page_dir = 'pages/'

template = '''
<head>
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?bb1a4de82e3332e4b957c7d83b3f7095";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();
</script>
'''


template_index='''
<li><p><a target="_blank" href='pages/{{name}}.html'><span>{{name}}</span></a></p></li>
'''

article_list=[]
for file in os.listdir(page_dir):
    article_list.append(file.replace('.html', ''))
    path = os.path.join(page_dir, file)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    if 'hm.baidu.com' in html:
        print('processed')
        continue
    html = html.replace('<head>', template)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)


with open('static/template/pages.html', 'r', encoding='utf-8') as f:
    html = f.read()
index_content=''
for file_name in article_list:
    index_content=index_content+template_index.replace('{{name}}',file_name)+'\n'
with open('pages.html', 'w', encoding='utf-8') as f:
    f.write(html.replace('{{index}}',index_content))