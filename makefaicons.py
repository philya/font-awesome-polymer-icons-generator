#!/usr/bin/env python

# Standard Library
import xml.etree.ElementTree as ET
from decimal import Decimal

# Vendor Libraries
import yaml
from jinja2 import Template

def build(iconset_id='fa', include_ids=[]):
    tree = ET.parse('res/fontawesome-webfont.svg')
    root = tree.getroot()
    namespaces = {'svg': 'http://www.w3.org/2000/svg'}

    glyph_map = {}
    for glyph in root.findall('.//svg:glyph', namespaces):
        glyph_map[hex(ord(glyph.get('unicode')))[2:]] = glyph

    iconsdf = open('res/icons.yml', 'r')
    iconsd = yaml.load(iconsdf)
    iconsdf.close()

    icond_map = {}
    for ii in iconsd['icons']:      
        icond_map[ii['unicode']] = ii

    default_width = 1792

    glyphs = []
    
    for key, idef in icond_map.items():
        if key in glyph_map:
            glyph = idef
            glyphel = glyph_map[key]
            glyph['d'] = glyphel.get('d')
            glyph['horiz-adv-x'] = glyphel.get('horiz-adv-x')

            scale = 1
            x_margin = 0
            if glyph['horiz-adv-x']:
                custom_width = int(glyph['horiz-adv-x'])
                if custom_width < default_width:
                    x_margin = (default_width - custom_width) / 2

                if custom_width > default_width:
                    scale = Decimal(float(default_width) / float(custom_width), 2).quantize(Decimal('0.0001'))

            glyph['x_margin'] = x_margin
            glyph['scale'] = str(scale)
            
            glyphs.append(glyph)

    context = {
        'iconset_id': iconset_id,
        'glyphs': glyphs,
        'default_width': default_width,
    }

    etemplatef = open('res/element-template.html', 'r')
    etemplate = Template(etemplatef.read())
    etemplatef.close()
    econtent = etemplate.render(**context)

    efile = open('build/fa-icons.html', 'w')
    efile.write(econtent)
    efile.close()


if __name__ == "__main__":
    main()
