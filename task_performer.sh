#!/bin/bash

folder="0x02-shell_redirections"
cfile="$folder/$1"

echo "#!/bin/bash" > $cfile
echo $2 >> $cfile

chmod u+x $cfile
git add .
git commit -m "Shell Redirection - $1"
git push

$cfile
