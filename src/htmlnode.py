class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    
    def to_html(self):
        raise NotImplementedError("Not implemented")
    
    def props_to_html(self):
        if self.props:
            return ' '.join(f'{key}="{value}"' for key, value in self.props.items())
        return ''

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        formatted_props = self.props_to_html()
        if self.tag:
            if formatted_props:
                return f"<{self.tag} {formatted_props}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"
        return ""


class ParentNode(HTMLNode):
    def __init__(self,tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag must be provided for HTML generation.")
        if not self.children:
            raise ValueError("ParentNode must contain at least one child to generate HTML.")

        formatted_props = self.props_to_html()
        opening_tag = f"<{self.tag} {formatted_props}".strip() + '>'
        closing_tag = f"</{self.tag}>"
        children_html = ''.join(child.to_html() for child in self.children)

        return f"{opening_tag}{children_html}{closing_tag}"

            


