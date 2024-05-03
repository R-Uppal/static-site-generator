import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single(self):
        node = HTMLNode(props={'id': 'main-content', "href": "https://boot.dev"})
        self.assertEqual(node.props_to_html(), 'id="main-content" href="https://boot.dev"')
    
    def test_html_with_all_attributes(self):
        node = LeafNode('p', 'Hello, world!', {'class': 'text-bold', 'id': 'greeting'})
        self.assertEqual(node.to_html(), '<p class="text-bold" id="greeting">Hello, world!</p>')



if __name__ == "__main__":
    unittest.main()

