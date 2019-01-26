# coding=utf-8

import pdfkit




def save_pdf(htmlFileName,pdfFileName):
    """
    把所有html文件保存到pdf文件
    :param htmls:  html文件列表
    :param file_name: pdf文件名
    :return:
    """

    path_wk = r'D:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # 安装位置
    configuration = pdfkit.configuration(wkhtmltopdf=path_wk)


    with open(htmlFileName) as f:
        pdfkit.from_file(f, pdfFileName,configuration=configuration)




