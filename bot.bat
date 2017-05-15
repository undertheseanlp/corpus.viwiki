set PYTHONIOENCODING=utf-8
call activate corpus.viwiki
python script.py
git add -A
git commit -m "update data"
git push origin master