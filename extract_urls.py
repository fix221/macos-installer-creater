import xml.etree.ElementTree as ET
import requests
import os

def parse_catalog(file_path):
    """ 解析XML目录文件并提取pkg URL。 """
    urls = []
    tree = ET.parse(file_path)
    root = tree.getroot()
    products = root.find('dict/dict/key[text()="Products"]/following-sibling::dict')

    for product in products:
        for package in product.find('dict/key[text()="Packages"]/following-sibling::array'):
            url = package.find('dict/key[text()="URL"]/following-sibling::string').text
            if url.endswith('.pkg'):
                urls.append(url)

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
    # catalog_file = os.path.join(os.getcwd(), 'index-26seed-26-15-14-13-12-10.16-10.15-10.14-10.13-10.12-10.11-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog')
    urls = parse_catalog(catalog_file)
    save_urls_to_file(urls)

if __name__ == "__main__":
    main()
