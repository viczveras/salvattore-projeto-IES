from flask import render_template, request, redirect, url_for, session, flash
from . import admin_bp
import os

SALVATTORE_ADMIN= 'salvattore_admin'
SALVATTORE_SENHA= 'salvattore2026'

arq_processos= 'processos.csv'

diretorio_base= os.path.dirname(os.path.abspath(__file__))
arquivo_processos= os.path.join(diretorio_base, '..', 'data', 'processos.csv')

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        usuario= request.form.get('usuario')
        senha= request.form.get('senha')

        if usuario == SALVATTORE_ADMIN and senha == SALVATTORE_SENHA:
            session['usuario_logado'] = usuario
            flash('Login realizado com sucesso!', 'sucesso')
            return redirect(url_for('admin.processos'))
        else:
            flash('Usuário ou senha incorretos.', 'erro')
    
    return render_template('admin/login.html')


@admin_bp.route('/logout')
def logout():
    session.pop('usuario_logado', None)
    flash('Logout realizado com sucesso!', 'sucesso')
    return redirect(url_for('pagina_principal'))

    

def ler_processos():

    processos=[]

    with open(arquivo_processos, 'r', encoding='utf-8') as arq:
        linhas = arq.readlines()

        for linha in linhas[1:]:
            linha = linha.strip()
            if not linha:
                continue

            processo_id,titulo,url = linha.split(',')

            processos.append({
                "processo_id": int(processo_id),
                "titulo": titulo,
                "url": url,
            })

    return processos


@admin_bp.route('/processos')
def processos():
    processos= ler_processos()

    if 'usuario_logado' not in session:
        flash('Você não esta logado', 'erro')
        return redirect(url_for('admin.login'))

    return render_template('admin/processos.html', processos= processos)


@admin_bp.route('/novo', methods=['GET','POST'])
def novo_processo():
    
    if 'usuario_logado' not in session:
        flash('Você não está logado.', 'erro')
        return redirect(url_for('admin.login'))
    
    if request.method=='GET':
        return render_template('admin/criar_processo.html')
    
    if request.method=='POST':
        titulo= request.form.get('titulo')
        url= request.form.get('url')

        processos=ler_processos()

        maior_id=0

        for processo in processos:
            if processo['processo_id']>maior_id:
                maior_id=processo['processo_id']
    
        novo_id=maior_id+1

        nova_linha=f"\n{novo_id},{titulo},{url}"

        with open(arquivo_processos, 'a', encoding='utf-8') as arq:
            arq.write(nova_linha)
    
    return redirect(url_for('admin.processos'))


@admin_bp.route('/editar/<int:processo_id>', methods=['GET', 'POST'])
def editar_processo(processo_id):

    processos= ler_processos()

    processos_reescrita=[]
    
    if request.method== 'GET':

        processo_encontrado= None

        for processo in processos:
            if processo['processo_id']== processo_id:
                processo_encontrado=processo
                break
        
        return render_template('admin/editar_processo.html', processo=processo_encontrado)
    
    if request.method== 'POST':

        titulo_novo= request.form.get('titulo')
        url_nova= request.form.get('url')


        for processo in processos:
            if processo['processo_id'] != processo_id:
                processos_reescrita.append(processo)
        
        processos_reescrita.append(
            {
                'processo_id': processo_id,
                'titulo': titulo_novo,
                'url': url_nova,
            }
        )
                   
    with open(arquivo_processos, 'w', encoding='utf-8') as arq:
        arq.write("id,titulo,url\n")
        for processo in processos_reescrita:
            linha= f"{processo['processo_id']},{processo['titulo']},{processo['url']}\n"
            arq.write(linha)
    
    return redirect(url_for('admin.processos'))


@admin_bp.route('/deletar/<int:processo_id>', methods=['GET', 'POST'])
def deletar_processo(processo_id):

    processos=ler_processos()

    processos_reescrita=[]

    for processo in processos:
        if processo['processo_id'] != processo_id:
            processos_reescrita.append(processo)
    
    with open(arquivo_processos, 'w', encoding='utf-8') as arq:
        arq.write("id,titulo,url\n")
        for processo in processos_reescrita:
            linha= f"{processo['processo_id']},{processo['titulo']},{processo['url']}\n"
            arq.write(linha)
    
    return redirect(url_for('admin.processos'))