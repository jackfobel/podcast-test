import yaml
import xml.etree.ElementTree as xml_tree

# https://github.com/jackfobel/podcast-test
# https://github.com/jackfobel/podcast-generator

# RSS Feed example from Apple
# https://help.apple.com/itc/podcasts_connect/#/itcbaf351599

# This program reads in a yaml file containing various podcasts and creates an RSS feed file
#   in xml format. It also uses GitHub pages to host the files at:
#   https://jackfobel.github.io/podcast-test/
#
# Process: If someone modifies the feed.yaml file, a GitHub Action is called to run this python script
#   which generates a new podcast.xml file and push things onto the server.


with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

    rss_element = xml_tree.Element('rss', {'version':'2.0',
        'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd',
        'xmlns:content':'http://purl.org/rss/1.0/modules/content/'})

channel_element = xml_tree.SubElement(rss_element, 'channel')

link_prefix = yaml_data['link']

xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']
xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']
xml_tree.SubElement(channel_element, 'format').text = yaml_data['format']
xml_tree.SubElement(channel_element, 'subtitle').text = yaml_data['subtitle']
xml_tree.SubElement(channel_element, 'itunes:author').text = yaml_data['author']
xml_tree.SubElement(channel_element, 'description').text = yaml_data['description']
xml_tree.SubElement(channel_element, 'itunes:image', {'href': link_prefix + yaml_data['image']})
xml_tree.SubElement(channel_element, 'language').text = yaml_data['language']
xml_tree.SubElement(channel_element, 'link').text = link_prefix
xml_tree.SubElement(channel_element, 'itunes:category', {'text': yaml_data['category'] })

for item in yaml_data['item']:
    item_element = xml_tree.SubElement(channel_element, 'item')
    xml_tree.SubElement(item_element, 'title').text = item['title']
    xml_tree.SubElement(item_element, 'itunes:author').text = yaml_data['author']  # same author for all
    xml_tree.SubElement(item_element, 'itunes:description').text = item['description']
    xml_tree.SubElement(item_element, 'itunes:duration').text = item['duration']
    xml_tree.SubElement(item_element, 'pubDate').text = item['published']
    xml_tree.SubElement(item_element, 'title').text = item['title']

    enclosure = xml_tree.SubElement(item_element, 'enclosure', {
        'url': link_prefix + item['file'],
        'type': 'audio/mpeg',
        'length': item['length']
    })


output_tree = xml_tree.ElementTree(rss_element)

# creates a podcast.xml file
output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)
