from flask import Blueprint, request, redirect, render_template, url_for

from services.code_generator import gerar_code
from database.repository import salvar, get_original_url

main = Blueprint("main", __name__)

@main.route('/', methods=['GET', 'POST'])
def home():

    short_url = None

    if request.method == 'POST':
        url = request.form.get('url')

        if url:
            code = gerar_code()
            salvar(code, url, None)

            short_url = url_for("main.redirect_page", codigo=code, _external=True)

    return render_template(
        'index.html',
        short_url=short_url
    )

@main.route('/link/<codigo>', methods=['GET'])
def redirect_page(codigo):
    original_url = get_original_url(codigo)
    
    if original_url:
        return redirect(original_url)

    return "link não encontrado", 404