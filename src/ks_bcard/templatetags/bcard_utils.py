'''
Utility template tags for ksystems-businesscard
'''
from django import template
from django.template.base import Node

register = template.Library()

class VerbatimNode(template.Node):
    '''
    This class is here for {% verbatim %} tag
    '''
    def __init__(self, text):
        self.text = text
    
    def render(self, context):
        return self.text


@register.tag
def verbatim(parser, token):
    '''
    We only keep it this way because default {% verbatim %} support
    will come in django 1.5 and the one in trunk seems broken.
    '''
    text = []
    while 1:
        token = parser.tokens.pop(0)
        if token.contents == 'endverbatim':
            break
        if token.token_type == template.TOKEN_VAR:
            text.append('{{')
        elif token.token_type == template.TOKEN_BLOCK:
            text.append('{%')
        text.append(token.contents)
        if token.token_type == template.TOKEN_VAR:
            text.append('}}')
        elif token.token_type == template.TOKEN_BLOCK:
            text.append('%}')
    return VerbatimNode(''.join(text))