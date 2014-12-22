
Genearte a Polymer/core-icon compatible Font Awesome SVG icon set.

# Set Up

    git clone https://github.com/philya/font-awesome-polymer-icons-generator.git pfa
    cd pfa
    mkvirtualenv pfa
    pip install -r requirements.pip

# Usage

    ./makefaicons.py <iconset-id> [icon_id1] [icon_id2] ...

## Full FA Icon Set (Development)

Using the full iconset is not recommended for production. For use in production, always specify icon ids you need in your iconset. (See next section)

To generate full Font Awesome iconset, run

    ./makefaicons.py fa

This will create two files

    build/fa-icons.html
    build/demo.html

To test your resulting iconset, run a simple webserver:

    cd build
    python -m SimpleHTTPServer

And direct your browser to

    http://localhost:8000/demo.html

Then, use your FA icons in polymer like this:

    <core-icon icon="fa:line-chart"></core-icon>

## Choose Specific Icons (Production)

For example:

    ./makefaicons.py myappname code line-chart github-alt

This will generate two files:

    build/myappname-icons.html
    build/demo.html

Then, use your FA icons in polymer like this:

    <core-icon icon="myappname:line-chart"></core-icon>
