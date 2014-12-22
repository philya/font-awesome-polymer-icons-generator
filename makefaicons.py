#!/usr/bin/env python
import xml.etree.ElementTree as ET
import yaml

def main():
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

    glyphs_out = open('build/glyphs.out', 'w')

    for key, idef in icond_map.items():
        print key, idef['id']
        if key in glyph_map:
            #print glyph_map[key].get('d')
            glyphs_out.write('<g id="%s"><path d="%s"/></g>\n' % (idef['id'], glyph_map[key].get('d')))


    glyphs_out.close()




if __name__ == "__main__":
    main()
