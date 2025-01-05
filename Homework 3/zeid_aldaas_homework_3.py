# -*- coding: utf-8 -*-
"""Zeid Aldaas Homework 3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1R1CDFOLI5gAjBtzbPrK926fp1PV8Gwu7
"""

# 1. The following questions use the data collected from the anonymous survey collected at the beginning of the course and from previous semesters. The dataset can be downloaded from the module on Canvas.
# Apply Pandas queries, manipulation, grouping, and aggregating to answer these questions.
!pip install pandas
import pandas as pd
survey = pd.read_csv("surveydataFall2024.csv")
survey

# a. Show only rows where Statistics skill is 10
survey[survey["Statistics"] == 10]

# b. Show only rows where both Statistics and Math skills are 10
survey[survey["Statistics"] == 10][survey["Math"] == 10]

# c. Show only the Semester, Communication, and Visualization columns where both Statistics and Math skills are 10
survey[survey["Statistics"] == 10][survey["Math"] == 10][["Semester", "Communication", "Visualization"]]

# d. Show only the Semester, Communication, and Visualization columns in decreasing order of Statistics and then Math skills
survey.sort_values(by=["Statistics", "Math"], ascending=False)[["Semester", "Communication", "Visualization"]]

# e. Show only rows where Statistics skill is missing
survey[survey["Statistics"].isna()]

# f. Show for every student, only their Semester, Math skill, Statistics skill, and the maximum of their Math and Statistics skills (Hint: use axis=1)
survey[["Semester", "Math", "Statistics"]].assign(Max=survey[["Math", "Statistics"]].max(axis=1))

# g. Show the median value of Computer Science skills
survey["ComputerScience"].median()

# h. Show the median value of Computer Science skills in Fall 2023
survey[survey["Semester"] == "Fall2023"]["ComputerScience"].median()

# i. Show the median values of (each of) Computer Science, Math, and Statistics skills in every semester
survey.groupby("Semester")[["ComputerScience", "Math", "Statistics"]].median()

# j. Show the median values of (each of) Computer Science, Math, and Statistics skills in every semester of students who have taken CPSC483 (TakenCPSC483 is Yes)
survey[survey["TakenCPSC483"] == "Yes"].groupby("Semester")[["ComputerScience", "Math", "Statistics"]].median()

# k. Show the median values of (each of) Computer Science, Math, and Statistics skills for groups of students who have taken and not taken CPSC483 (Hint: groupby)
survey.groupby("TakenCPSC483")[["ComputerScience", "Math", "Statistics"]].median()

# l. Show the number of students who took the survey in every semester
survey.groupby("Semester").size()

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