from docxtpl import DocxTemplate, InlineImage
from docx.shared import Inches
from datetime import date
from babel.dates import format_date
import locale

# set locale to indonesian
# locale.setlocale(locale.LC_TIME, "id")

# get todays date
today = format_date(date.today(),  "d MMMM Y", locale="id_ID")
operational_date = format_date(date.today(), "d-M-Y", locale="id_ID")

doc = DocxTemplate('docs/template/template.docx')

images = [InlineImage(doc,'img/cat3.jpg', width=Inches(3)) for x in range(4)]
context = {
    'nama' : 'Wahyu Miftahul Ganteng',
    'images' : images,
    'tanggal_buat' : today,
    'tanggal_operasi' : "28-02-2019"
}

doc.render(context)


doc.save('docs/result/tes.docx')


# import locale

# alllocale = locale.locale_alias
# for k in alllocale.keys():
#     print('locale[%s] %s' % (k, alllocale[k]))   