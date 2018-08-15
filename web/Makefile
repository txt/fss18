
build:
	mkdocs build
	cp docs/404.html site/
	cp -r site/* ../docs
	- git add  ../docs/* 
	- git add ../docs/*/*
	- git add ../docs/*/*/*
	git commit -am as
	git push

serve:
	mkdocs serve
