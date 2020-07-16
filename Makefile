run-fresh:
	docker build --no-cache -t foo . && docker run -it foo
