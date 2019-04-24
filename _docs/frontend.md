```
rm -rf dist/*
yarn build
mv dist/static/js dist/js
rm -rf dist/static/
cat dist/index.html | sed 's/\/css\//\/static\/css\//g' > dist/temp.html
mv dist/temp.html dist/index.html
```

cp -R dist/* ../backend/static/
