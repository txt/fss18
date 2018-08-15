
build:
	mkdocs build
	cp -r site/* ../docs
	- git add  ../docs/* 
	- git add ../docs/*/*
	- git add ../docs/*/*/*
	git commit -am as
	git push

serve:
	mkdocs serve
