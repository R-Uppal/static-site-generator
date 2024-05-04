import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single(self):
        node = HTMLNode(props={'id': 'main-content', "href": "https://boot.dev"})
        self.assertEqual(node.props_to_html(), 'id="main-content" href="https://boot.dev"')
    
    def test_html_with_all_attributes(self):
        node = LeafNode('p', 'Hello, world!', {'class': 'text-bold', 'id': 'greeting'})
        self.assertEqual(node.to_html(), '<p class="text-bold" id="greeting">Hello, world!</p>')
    
    def test_parent_node_with_children(self):
        children = [
            LeafNode('b', 'Bold text'),
            LeafNode(None, ' and '),
            LeafNode('i', 'italic text')
        ]
        parent = ParentNode('p', children)
        expected_html = '<p><b>Bold text</b> and <i>italic text</i></p>'
        self.assertEqual(parent.to_html(), expected_html)



if __name__ == "__main__":
    unittest.main()

