# -*- coding: utf-8 -*-
"""Zeid Aldaas Homework 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_hkIBaJejskxAmlWstRcan1APyCiiGhh
"""

# Task 1
from google.colab import files
from IPython.display import Image

uploaded = files.upload()
Image(filename="HeadshotName.jpg")

# Task 2
import statsmodels.api as sm

mtcars_dataset = sm.datasets.get_rdataset("mtcars")
mtcars = mtcars_dataset.data

# Questions and Answers
# a. How many rows are there?
print(f"a. Number of rows: ", len(mtcars))

# b. How many columns are there?
print(f"b. Number of columns: ", len(mtcars.columns))

# c. What is the unit of the weight column?
print("c.\n------------------------------")
help(mtcars_dataset)
print(f"------------------------------\nUnit of weight column: lb\n")

# d. Show first 10 rows.
print(f"d. First 10 rows:\n", mtcars.head(10), "\n")

# e. Show every other row.
print(f"e. Every other row:\n", mtcars.iloc[::2], "\n")

# f. Show all rows where the number of cylinders is 4 or 6.
print(f"f. Rows where number of cylinders is 4 or 6:\n", mtcars[(mtcars["cyl"] == 4) | (mtcars["cyl"] == 6)], "\n")

# g. Are there any NAs in the mpg column?
nasum = mtcars["mpg"].isna().sum()
if(nasum > 0):
  print(f"g. Yes, there are {nasum} NAs in the mpg column.")
else:
  print(f"g. No, there are no NAs in the mpg column.")

# h. What is the mean mpg value?
mean_mpg = mtcars["mpg"].mean()
print(f"h. Mean mpg value: {mean_mpg}")

# i. Show all rows where mpg is lower than the mean mpg value?
print(f"i. Rows where mpg is lower than the mean mpg value:\n", mtcars[mtcars["mpg"] < mean_mpg], "\n")

# j. What is the horsepower of the car with the highest mpg?
maxmpg = mtcars["mpg"].idxmax()
print(f"j. The horsepower of the car with the highest mpg: {mtcars.loc[maxmpg, 'hp']}")

# Task 3
#Stack Overflow (https://stackoverflow.com) is an active community where Python and data science are frequently discussed. Users post questions related to all aspects of Python, including troubleshooting code, understanding algorithms, and choosing the right libraries for data science tasks. The community is highly active, with questions often being answered within minutes. Users range from beginners to experts in Python and data science, and the community is generally friendly, although detailed, well-researched questions are more likely to receive positive responses. It's a helpful space for newcomers, provided they follow community guidelines and clearly explain their problems.

# Commented out IPython magic to ensure Python compatibility.
def colab2pdf():
  # @title Download Notebook in PDF Format{display-mode:'form'}
  !apt-get install -yqq --no-install-recommends librsvg2-bin>/dev/null;
  import contextlib,datetime,google,io,IPython,ipywidgets,json,locale,nbformat,os,pathlib,requests,urllib,warnings,werkzeug,yaml,re;locale.setlocale(locale.LC_ALL,'en_US.UTF-8');warnings.filterwarnings('ignore',category=nbformat.validator.MissingIDFieldWarning);
#   %matplotlib inline
  def convert(b):
    try:
      s.value='🔄 Converting';b.disabled=True
      n=pathlib.Path(werkzeug.utils.secure_filename(urllib.parse.unquote(requests.get(f'http://{os.environ["COLAB_JUPYTER_IP"]}:{os.environ["KMP_TARGET_PORT"]}/api/sessions').json()[0]['name'])))
      p=pathlib.Path('/content/pdfs')/f'{datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")}_{n.stem}';p.mkdir(parents=True,exist_ok=True);nb=nbformat.reads(json.dumps(google.colab._message.blocking_request('get_ipynb',timeout_sec=600)['ipynb']),as_version=4)
      u=[u for c in nb.cells if c.get('cell_type')=='markdown' for u in re.findall(r'!\[.*?\]\((https?://.*?)\)',c['source']) if requests.head(u,timeout=5).status_code!=200]
      if u:raise Exception(f"Bad Image URLs: {','.join(u)}")
      nb.cells=[cell for cell in nb.cells if '--Colab2PDF' not in cell.source]
      nb=nbformat.v4.new_notebook(cells=nb.cells or [nbformat.v4.new_code_cell('#')]);nbformat.validator.normalize(nb)
      nbformat.write(nb,(p/f'{n.stem}.ipynb').open('w',encoding='utf-8'))
      with (p/'config.yml').open('w', encoding='utf-8') as f: yaml.dump({'include-in-header':[{'text':r'\usepackage{fvextra}\DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaksymbolleft={},showspaces=false,showtabs=false,breaklines,breakanywhere,commandchars=\\\{\}}'}],'include-before-body':[{'text':r'\DefineVerbatimEnvironment{verbatim}{Verbatim}{breaksymbolleft={},showspaces=false,showtabs=false,breaklines}'}]},f)
      !quarto render {p}/{n.stem}.ipynb --metadata-file={p}/config.yml --to pdf -M latex-auto-install -M margin-top=1in -M margin-bottom=1in -M margin-left=1in -M margin-right=1in --quiet
      google.colab.files.download(str(p/f'{n.stem}.pdf'));s.value=f'✅ Downloaded: {n.stem}.pdf'
    except Exception as e:s.value=f'❌ {str(e)}'
    finally:b.disabled=False
  if not pathlib.Path('/usr/local/bin/quarto').exists():
    !wget -q 'https://quarto.org/download/latest/quarto-linux-amd64.deb' && dpkg -i quarto-linux-amd64.deb>/dev/null && quarto install tinytex --update-path --quiet && rm quarto-linux-amd64.deb
  b=ipywidgets.widgets.Button(description='⬇️ Download');s=ipywidgets.widgets.Label();b.on_click(lambda b:convert(b));IPython.display.display(ipywidgets.widgets.HBox([b,s]))
colab2pdf() # | Colab2PDF v1.6 | https://github.com/drengskapur/colab2pdf | GPL-3.0-or-later |