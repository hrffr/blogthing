import blagconfig
fdir = blagconfig.fdir
def updateMainPage(title, name):
	entries = lastFive()
	template = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>%s</title>
    <link href="style.css"
          title="Today"
          rel="stylesheet"
          type="text/css">
    <meta http-equiv="Default-Style"
          content="Today">
</head>
  <body>
  <div class=header>
  <header>
  </header>
  <nav>
  <ul>
  <li class=active><a href="index.html">Latest Posts</a></li>
  <li ><a href="archive.html">Archive</a></li>
  </ul>
  </nav>
  </div>
  <main>
  <article>

<h2>%s</h2>

<!-- build entries here 
<h3>Post title link here</h3>
<p>Post preview here</p>
-->
%s

  </article>
  </main>
</html>

""" % (title, name, entries)
	return template

def lastFive():
	entries = open(fdir+"/fname2title.txt").read()
	entries = entries.split("\n")
	earray = []
	for i in range(len(entries)-1):
		earray.append(entries[i])
	earray.reverse()
	five = []
	for i in range(0, len(earray)):
		five.append(earray[i])
	
	entrystr = ""
	for i in range(len(five)):
		current_entry = five[i].split("|")
		filename = current_entry[0]
		date = current_entry[1]
		title = current_entry[2]
		desc = current_entry[3]
		entrystr += """
<p><a href="%s"><h3>%s</h3></a>
%s<br><sup>%s</sup></p>

		""" % (filename, title, desc, date)
		if i == 4:
			break
	return entrystr


def buildPost(content, title, name, date, posttitle):
	template = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>%s - %s</title>
    <link href="style.css"
          title="Today"
          rel="stylesheet"
          type="text/css">
    <meta http-equiv="Default-Style"
          content="Today">
</head>
  <body>
  <div class=header>
  <header>
  </header>
  <nav>
  <ul>
  <li ><a href="index.html">Index</a></li>
  <li ><a href="archive.html">Archive</a></li>
  </ul>
  </nav>
  </div>
  <main>
  <article>

<h2>%s</h2> <sup>%s</sup>

<h3>%s</h3>
%s

  </article>
  </main>
</html>
""" % (title, posttitle, name, date, posttitle, content)
	return template
