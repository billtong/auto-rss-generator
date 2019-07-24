from xml.etree import ElementTree
from datetime import datetime

def auto_generate_xml(entry_dic_list):
    ElementTree.register_namespace("", "http://www.w3.org/2005/Atom")
    et = ElementTree.parse("server/rss_template.xml")
    update = ElementTree.SubElement(et.getroot(), "updated")

    latest_updated = entry_dic_list[0]["published"]
    '''
    need to check the latest publish date here to make sure.
    
    '''
    update.text = latest_updated
    for entry_dic in entry_dic_list:
        print(entry_dic)
        new_entry = ElementTree.SubElement(et.getroot(), "entry")
        title_tag = ElementTree.SubElement(new_entry, "title")

        title_tag.text = entry_dic["title"]
        link_tag = ElementTree.SubElement(new_entry, "link")
        link_tag.attrib["rel"] = "alternate"
        link_tag.attrib["type"] = "text/html"
        link_tag.attrib["href"] = entry_dic["link"]
        id_tag = ElementTree.SubElement(new_entry, "id")
        id_tag.text = entry_dic["id"]
        publish_tag = ElementTree.SubElement(new_entry, "published")
        publish_tag.text = entry_dic["published"]
    et.write("server/slack_devops_channel_rss.xml", encoding='utf-8', xml_declaration=True)