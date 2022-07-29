def generate_html(data):
  html = '''
  <!DOCTYPE html>
  <html lang="en">
      <body>
      <h1>INEC NEWS!<h1>
  '''

  for i in range(len(data)):
    html = html + f'''
    <h2>{data[i]["date"]}</h2>
    <h4>{data[i]["title"]}</h4>
    <hr>
    '''

  return html + '''
      </body>
  </html>'''

# print(generate_html([{"title": "Screw Buhari", "date": "1st jan"}, {"title": "Screw Atiku", "date": "1st jan"}]))