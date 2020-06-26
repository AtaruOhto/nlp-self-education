```
docker build ./ -t nlp-learning
```

```bash
# bash
docker run --name nlp-learning --mount type=bind,src=$(pwd)/,dst=/learning  -it --rm nlp-learning /bin/bash 
```

```bash
# fish
docker run --name nlp-learning --mount type=bind,src=$(pwd)/,dst=/learning  -it --rm nlp-learning /bin/bash 
```


```bash
poetry run python nlp/simple.py 
```