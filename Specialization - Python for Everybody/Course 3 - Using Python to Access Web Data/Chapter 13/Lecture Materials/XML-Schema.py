'XML Schema'
#Describing a "contact" as to what is acceptable in XML.
#   -Description of the legal format of an XML document
#   -Expressed in terms of constraints on the structure and content of documents.
#   -Often used to specify a "contract" between systems - "My system will only accept XML that conforms to this particular Schema."
#   -If a particular piece of XML meets the specification of the Schema - it is said to "validate"
#Validation is the act of verifying that the data is in the right format.
'''             ---XML Document---
    <person>
        <lastname>Severance</lastname>
        <age>17</age>
        <dateborn>2001-04-17</dateborn>
    </person>
                                                    >|Validator|
            ---XML Schema Contact---
    <xs:complexType name="person">
        <xs:sequence>
            <xs:element name="lastname" type="xs.string"/>
            <xs:element name="age" type="xs.integer"/>
            <xs:element name="datebornn" type="xs.date"/>
        </xs:sequence>
    <\xs:complexType>
'''

'Many XML Schema Languages'
# Document Type Definition (DTD)
#       http://en.wikipedia.org/wiki/Document_Type_Definition
# Standard Generalized Markup Language (ISO 8879:1986 SGML)
#       http://en.wikipedia.org/wiki/SGML
# XML Schema from W3C - (XSD)
#       http://en.wikipedia.org/wiki/XML_Schema_(W3C)

'XSD XML Schema (W3C spec)'
#We will focus on the World Wide Web Consortium (W3C) version
#It is often called "W3C Schema" because "Schema" is considered generic
#More commonly it is called XSD because the file names end in .xsd

'''             XSD Structure
        XML documents
    <person>                                ->xs:complexType
        <lastname>Severance</lastname>      ->xs:element
        <age>17</age>                       ->xs:element
        <dateborn>2001-04-17</dateborn>     ->xs:element
    </person>                               ->xs:complexType

            ---XML Schema Contact---
    <xs:complexType name="person">                          ->xs:complexType
        <xs:sequence>                                       ->xs:sequence
            <xs:element name="lastname" type="xs.string"/>  ->xs:element
            <xs:element name="age" type="xs.integer"/>      ->xs:element
            <xs:element name="datebornn" type="xs.date"/>   ->xs:element
        </xs:sequence>                                      ->xs:sequence
    <\xs:complexType>                                       ->xs:complexType

-------------------------------------------------------------------------------
                        XSD Constraints
SCHEMA
<xs:element name="person">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="full_name" type="xs:string" minOccurs="1" maxOccurs="1" />
            <xs:element name="child_name" type="xs:string" minOccurs="0" maxOccurs="10" />
        </xs:element name="person">
    </xs:complexType>
</xs:sequence>

XML
<person>
    <full_name>Tove Refsnes</full_name>
    <child_name>Hege</child_name>
    <child_name>Stale</child_name>
    <child_name>Jim</child_name>
    <child_name>Borge</child_name>
</person>
-------------------------------------------------------------------------------
                        XSD Data Types
XSD
<xs:element name="customer" type="xs:string"/>
<xs:element name="start" type="xs:date"/>
<xs:element name="startdate" type="xs:dateTime"/>
<xs:element name="prize" type="xs:decimal"/>
<xs:element name="weeks" type="xs:integer"/>

XML
<customer>John Smith</customer>
<start>2002-09-24</start>       #4digityear-2dMonth-2dDay; easy for sorting
<startdate>2002-05-30T09:30:10Z</startdate> #It is common to represent time in UCT/GMT, given that servers are often scattered around the world
<prize>999.50</prize>
<weeks>30</weeks>
-------------------------------------------------------------------------------
        ISO 8601 Date/Time Format
  2002-05-30T09:30:10Z <-timezone - typically specified in UCT/GMT rather than local time zone.
  y/m/d      time of day 
  
'''
