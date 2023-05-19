'Data on the Web'
#With the HTTP Request/Response well understood and well supported, there was a natural move toward exchanging data between programs using these protocols
#We needed to come up with an agreed way to represent data going between aplications and across networks
#There are two commonly used formats: XML and JSON

'Sending Data across the "Net"'
#|  Python   |                  |  Java |
#|Dictionary | --> (cloud) -->  |HashMap|

#aka "Wire Protocol" - What we send on the "wire"

'Agreeing on a "Wire Format"' #XML - an agreed on intermediate protocol that is just text. not internal memory
#| Python   |serialize  (<person>)  de-serialize | Java  | the act of going from an internal representation from one computer
#|Dictionary|---------> (<name>...) -----------> |HashMap| out to a interchanged format is called serialization
'''XML #XML is the older                JSON
<person>  of the two,                       {
 <name> and more rigorous one                 "name":
  Chuck                                        "Chuck",
 </name>                                      "phone":
 <phone>                                        "303-4456"
  303 4456                                  }
 </phone>
</person>
''' #data oriented documents, instead of human-readable arguments
#allows two different language users come to peace
