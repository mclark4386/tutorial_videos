def root():
    return """
<html><head><title>Testing Bottle</title></head>
<body>
%s<br />
%s
</body>
</html>
""" % (world(), form())


def world():
    return '<a href="/hello/world">World!</a>'


def form():
    return """
<div>
<input id="name" type="text" />
<input type="submit"
    onclick='window.location =
      "/hello/"+document.getElementById("name").value;'
    value="Submit" />
</div>
"""
