# -*- coding: utf-8 -*-

from scrape_tools import scrape_site

PUSHOVER_TOKEN = 'a1mw2jwknwzc7i3etxvemjdndxeeo1'
TITLE = 'Ticketswap.com'


def main():
    scrape_site(get_elements, get_attrs, get_next_page, TITLE, ad_string_format,
                pushover_token=PUSHOVER_TOKEN)


def get_elements(page):
    return page.find('div', class_='css-zmr4by e151mj0c1').findAll('a')


def get_next_page(page, _page_url):
    return None


def get_attrs(ad_element, ad_dict, search):
    href = ad_element.attrs["href"]
    ad_id = href[-10:]

    num_tickets = ad_element.find('h4', 'css-11rlpdz eh8fd905').get_text(strip=True)
    ticket_type = ad_element.find('span', 'css-vj5viy eh8fd903').get_text(strip=True)
    title = f'{num_tickets} ({ticket_type.lower()})'

    price = ad_element.find('strong', class_='css-tlq7v e1pkfxq11').get_text(strip=True)

    description = ad_element.find('span', 'css-1qji7c4 e6fq7ah4')
    if description:
        description = description.get_text(strip=True)

    ad_dict[ad_id] = dict(
        href=href,
        title=title,
        price=price,
        search=search,
        description=description
    )

    return ad_dict


def ad_string_format(ad_link, search_link, ad_dict):
    description = f'\n{ad_dict["description"]}' if ad_dict["description"] else ''
    return f'{ad_link} – {ad_dict["price"]} ({search_link}){description}'


if __name__ == '__main__':
    main()
