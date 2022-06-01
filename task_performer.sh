#!/bin/bash

# folder="0x02-shell_redirections"
folder="0x03-shell_variables_expansions"
cfile="$folder/$1"

echo "#!/bin/bash" > $cfile
echo $2 >> $cfile

chmod u+x $cfile
git add .
git commit -m "Shell Redirection - $1"
git push

$cfile
