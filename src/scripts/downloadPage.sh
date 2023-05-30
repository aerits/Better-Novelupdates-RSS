download_page () {
    w3m -dump_source $1 -o accept_encoding='*;q=0'
}

download_page () {
    w3m -dump_source $1 -o accept_encoding='*;q=0'
}
if [ $2 -eq 0 ]
then
    download_page $1 | grep shortlink | cut -d"=" -f4
elif [ $2 -eq 1 ]
then
     download_page $1 | grep chp-release | head -n 2 | tail -n 1 | cut -d"/" -f5
else
    echo "ENTER VALID COMMAND"
fi
