import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "url")
        node2 = TextNode("This is a text node", "bold", "url")
        self.assertEqual(node, node2)
    
    def test_not_eq_different_text(self):
        node = TextNode("Text A", "bold", "url")
        node2 = TextNode("Text B", "bold", "url")
        self.assertNotEqual(node, node2)

    def test_not_eq_different_text_type(self):
        node = TextNode("Text", "bold", "url")
        node2 = TextNode("Text", "italic", "url")
        self.assertNotEqual(node, node2)

    def test_not_eq_different_url(self):
        node = TextNode("Text", "bold", "url1")
        node2 = TextNode("Text", "bold", "url2")
        self.assertNotEqual(node, node2)

    def test_eq_with_self(self):
        node = TextNode("Text", "bold", "url")
        self.assertEqual(node, node)

    def test_not_eq_with_none(self):
        node = TextNode("Text", "bold", "url")
        self.assertNotEqual(node, None)

    def test_not_eq_with_different_type(self):
        node = TextNode("Text", "bold", "url")
        self.assertNotEqual(node, 1234)  # Comparing with an integer

    def test_repr(self):
        node = TextNode("Text", "bold", "url")
        self.assertEqual(repr(node), "TextNode(Text, bold, url)")


if __name__ == "__main__":
    unittest.main()
