## Install with pip

```
pip install -e git+git://github.com/5monkeys/easyxml.git@develop#egg=easyxml
```

## Description
EasyXML is an easy and concise way to generate XML output in Python.  It uses a
custom attribute getter so element names can be specified directly in the code:

```py
  books = EasyXML('books')
  books.book(title='Example A')
  books.book.author(name='John Smith', age=57)
  books.book.publisher(name='Publisher A')
  books.book(title='Example B')
  books.book.author(name='Jane Doe', age=30)
  books.book.author(name='James Cutter', age=45)
  books.book.publisher(name='Publisher B')
  print str(books)
```

The above code produces the following XML:

```xml
  <books>
    <book title="Example A">
      <author age="57" name="John Smith"/>
      <publisher name="Publisher A"/>
    </book>
    <book title="Example B">
      <author age="30" name="Jane Doe"/>
      <author age="45" name="James Cutter"/>
      <publisher name="Publisher B"/>
    </book>
  </books>
```

You don't actually need to create every parent element, allowing the following
code to work:

```py
  root = EasyXML('root')
  root.a.b.c()
  root.a.b.c()
  root.a()
  root.a.b.c()
  root.a.b.c()
  print str(root)
```

The above code produces the following XML:

```xml
  <root>
    <a>
      <b>
        <c/>
        <c/>
      </b>
    </a>
    <a>
      <b>
        <c/>
        <c/>
      </b>
    </a>
  </root>
```

Creating an element returns that element, which can then be passed to helper
methods:

```py
  def material(primitive, ambient, diffuse):
      primitive.ambient(r=ambient[0], g=ambient[1], b=ambient[2])
      primitive.diffuse(r=diffuse[0], g=diffuse[1], b=diffuse[2])

  root = EasyXML('root')
  material(root.primitive(type='sphere'), (64, 0, 0), (192, 0, 0))
  material(root.primitive(type='cube'), (0, 64, 0), (0, 192, 0))
  print str(root)
```

The above code produces the following XML:

```xml
  <root>
    <primitive type="sphere">
      <ambient b="0" g="0" r="64"/>
      <diffuse b="0" g="0" r="192"/>
    </primitive>
    <primitive type="cube">
      <ambient b="0" g="64" r="0"/>
      <diffuse b="0" g="192" r="0"/>
    </primitive>
  </root>
```

## License

See [LICENSE](https://github.com/5monkeys/easyxml/blob/master/LICENSE)
