echo "Insira o diretório: "
read -e -d dir 
git log --since=yesterday | grep "Added\|Started" | sed -e "s/^/***/g" >> $dir
