set PYTHONIOENCODING=utf-8
call activate corpus.viwiki
python script.py
python report\report.py
git add -A
git commit -m "update data"
git push origin master