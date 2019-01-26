from  lxml import etree

html = """
    <html>
    <body>
    <ul>
     <li>1
         <a href="">子</a>
     </li>
     <li>2
        <a href="">子</a>
     </li>
     <li>3
        <a href="">子</a>
     </li>
     <li>4
         <a href="">子</a>
     </li>
     <li>5
        <a href="">子</a>
     </li>
     
 </ul>
 </body>
 </html>
"""

x_data = etree.HTML(html)

# 下标 是从 mark 1开始;
result = x_data.xpath('//li[5]/text()') # ['5\n        ', '\n     ']

#  只能取 平级关系的标签
# result = x_data.xpath('//a[2]')  # 结果[] 空的 a没有同级


# result = x_data.xpath('/html/body/ul/li/a/text()')

print(result)