import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single(self):
        node = HTMLNode(props={'id': 'main-content', "href": "https://boot.dev"})
        self.assertEqual(node.props_to_html(), 'id="main-content" href="https://boot.dev"')



if __name__ == "__main__":
    unittest.main()

