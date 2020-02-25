import json

import xlrd as xlrd
from django.http import QueryDict


class ExcelImport:
    @staticmethod
    def get_cases(request):
        f = request.FILES.get('file_name')

        if f is None:
         return
        excel_type = f.name.split('.')[1]
        if excel_type in ['xlsx', 'xls'] :
            # 开始解析上传的excel表格
            wb = xlrd.open_workbook(filename=None, file_contents=f.read())
            table = wb.sheets()[0]
            cols = table.ncols  # 总列数
            rows = table.nrows
            exclelist = []
            for c in range(3, cols):
                context = {}
                context["other"] = {}
                context["id"] = c + 1
                context["var"] = {}
                for i in range(1, rows):
                    if "other" in str(table.row(i)[2]):
                        context["other"][table.row(i)[0].value] = {}
                        context["other"][table.row(i)[0].value]["desc"] = table.row(i)[1].value
                        context["other"][table.row(i)[0].value]["postion"] = table.row(i)[2].value
                        context["other"][table.row(i)[0].value]["value"] = table.row(i)[c].value
                    else:
                        context["var"][table.row(i)[0].value] = {}
                        context["var"][table.row(i)[0].value]["desc"] = table.row(i)[1].value
                        context["var"][table.row(i)[0].value]["postion"] = table.row(i)[2].value
                        context["var"][table.row(i)[0].value]["value"] = table.row(i)[c].value
                exclelist.append(context)
            exclelist = json.dumps(exclelist)
            request.data.update({"exclelist": exclelist})
