download(){
    if [ ! -f bootstrap-3.3.2-dist.zip ]
    then
        wget https://github.com/twbs/bootstrap/releases/download/v3.3.2/bootstrap-3.3.2-dist.zip
    fi
    unzip bootstrap-3.3.2-dist.zip
}

if [ \( -d "static/css" \) -a \( -d "static/js" \) -a \( -d "static/fonts" \) ]
then 
    echo -e "All the css, js and font directory are present.\nExiting without doing nothing."
else 
    echo -e "js or css or fonts directory not present.\n Using bootstrap to populate."
    download
    if [ ! -d "static" ]
    then
        mkdir static
    fi
    mv bootstrap-3.3.2-dist/* static/
    rmdir bootstrap-3.3.2-dist
    rm bootstrap-3.3.2-dist.zip
fi
