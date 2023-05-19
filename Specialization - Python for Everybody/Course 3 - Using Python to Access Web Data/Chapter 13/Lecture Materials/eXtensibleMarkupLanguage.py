'eXtensible Markup Language'
#Primary purpose is to help information systems share structured data
#It started as a simplified subset of the Standard Generalized Markup Language (SGML), and is designed to be relatively human-legible

'XML Basics' '''
<person> #! start tag
    <name>Chuck</name>
    <phone type = "intl"> #? attribute
    +1 734 303 4456 #* Text Content
    </phone>
    <email hide="yes"/> #! Self closing tag
</person> #* end tag

#* Line ends do not matter. White space is generally discarded on text elements. We ident only to be readable.
'''

'XML Terminology'
#!Tags indicate the beginning and ending of elements
#*Attributes - Keyword/value pairs on the opening tag of XML
#Serialize/De-Serialize - Convert data in one program into a common format thatcan be stored and/or transmitted
#                          between systems in a programming language-independent manner.

'XML as a Tree' '''
<a> <-- 'a node'
    <b>X</b> <-- 'X' is a text node and is a child of the B node
    <c> <--D node has two children
        <d>Y</d>
        <e>Z</e>
    </c>
</a>
''' 'XML Text and Attributes' '''
<a>
    <b>X</b>
    <c>
        <d>Y</d>
        <e>Z</e>
    </c>
</a>
'''
