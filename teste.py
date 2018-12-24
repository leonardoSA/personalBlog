@app.route("/noticia/<int:noticia_id>")
def noticia(noticia_id):
    noticia = noticias.find_one(id=noticia_id)  # query no banco de dados
    if noticia.get('imagem'):
        imagem_url = url_for('media', filename=noticia.get('imagem'))
    else:
        imagem_url = "http://placehold.it/100x100"

    noticia_html = u"""
        <h1>{titulo}</h1>
        <img src="{imagem_url}">
        <hr />
        <p>{texto}</p>
    """.format(
        imagem_url=imagem_url,
        **noticia
    )  # remember, Python is full of magic!

    return base_html.format(
        title=noticia['titulo'],
        body=noticia_html,
        logo_url=url_for('static', filename='generic_logo.gif')
    )