#! /bin/bash -ux
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

if [ ! -f static/js/typeahead.bundle.js ]
then
    echo -e "Downloading typeahead...\n"
    wget https://twitter.github.io/typeahead.js/releases/latest/typeahead.bundle.js
    mv typeahead.bundle.js static/js/
else
    echo -e "typeahead already present...\n"
fi

if [ ! -f static/js/jquery.min.js ]
then
    echo -e "Downloading jquery...\n"
    wget https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js
    mv jquery.min.js static/js/
else
    echo -e "jquery already present...\n"
fi

if [ ! -f static/js/handlebars-v3.0.0.js ]
then
    echo -e "Downloading handlebars...\n"
    wget http://builds.handlebarsjs.com.s3.amazonaws.com/handlebars-v3.0.0.js
    mv handlebars-v3.0.0.js static/js
else
    echo -e "handlebars already present...\n"
fi
