import xml.etree.ElementTree as ET
import requests
import os

def parse_catalog(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    # 假设你需要从 XML 中提取 URL，这里只是一个示例
    urls = [elem.text for elem in root.findall('.//url')]
    return urls

def save_urls_to_file(urls, output_file='pkg_urls.txt'):
    """ 将提取的URL保存到指定文件中。 """
    with open(output_file, 'w') as f:
        for url in urls:
            f.write(url + '\n')

def main():
    """ 主函数，解析目录文件并保存URL。 """
    # requests
    #https://swscan.apple.com/content/catalogs/others/index-26seed-26-15-14-13-12-10.16-10.15-10.14-10.13-10.12-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog
    catalog_file = 'https://swscan.apple.com/content/catalogs/others/index-26seed-26-15-14-13-12-10.16-10.15-10.14-10.13-10.12-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog'
    file = requests.get(catalog_file)
    file_path = os.path.join(os.getcwd(), 'index-26seed-26-15-14-13-12-10.16-10.15-10.14-10.13-10.12-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.xml')
    with open(file_path, 'wb') as f:
    # with open('index-26seed-26-15-14-13-12-10.16-10.15-10.14-10.13-10.12-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.xml', 'wb') as f:
        f.write(file.content)

    # local file
    # catalog_file = os.path.join(os.getcwd(), 'index-26seed-26-15-14-13-12-10.16-10.15-10.14-10.13-10.12-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog')
    urls = parse_catalog(file_path)
    save_urls_to_file(urls)

if __name__ == "__main__":
    main()
