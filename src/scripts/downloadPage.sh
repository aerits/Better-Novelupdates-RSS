download_page () {
    w3m -dump_source $1 -o accept_encoding='*;q=0'
}

download_page () {
    w3m -dump_source $1 -o accept_encoding='*;q=0'
}
download_page $1 | grep shortlink | cut -d"=" -f4
