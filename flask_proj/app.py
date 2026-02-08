from flask import Flask, jsonify, request, render_template, redirect, url_for
import json
import os

ARQUIVO_TAREFAS = os.path.join(os.path.dirname(__file__), 'tarefas.json')

tarefas = []
proximo_id = 1

def carregar_dado():
    global tarefas, proximo_id
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, 'r', encoding='utf-8') as f:
            data = json.load(f)
            tarefas = data['tarefas']
            proximo_id = data['proximo_id']

def salvar_dado():
    with open(ARQUIVO_TAREFAS, 'w', encoding='utf-8') as f:
        json.dump({'tarefas': tarefas, 'proximo_id': proximo_id}, f, ensure_ascii=False, indent=2)

carregar_dado()

def adicionar_tarefa(texto: str):
    global tarefas, proximo_id
    tarefas.append({
        'id': proximo_id,
        'texto': texto,
        'concluida': False
    })
    proximo_id += 1
    salvar_dado()
    return jsonify({'id': proximo_id - 1, 'texto': texto}), 201

def listar_tarefas():
    return jsonify(tarefas), 200

def atualizar_tarefa(id: int, texto: str):
    global tarefas
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefa['texto'] = texto
            return jsonify({'id': id, 'texto': texto}), 200
    return jsonify({'error': 'Tarefa não encontrada'}), 404

def concluir_tarefa(id: int):
    global tarefas
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefa['concluida'] = True
            salvar_dado()
            return jsonify({'id': id}), 200
    return jsonify({'error': 'Tarefa não encontrada'}), 404

def excluir_tarefa(id: int):
    global tarefas
    tarefas = [tarefa for tarefa in tarefas if tarefa['id'] != id]
    return jsonify({'id': id}), 200

app = Flask(__name__, template_folder='models')

@app.route('/')
def index():
    return render_template('index.html', tarefas=tarefas)

@app.route('/adicionar', methods=['POST'])
def adicionar_form():
    texto = request.form.get('texto_tarefa', '').strip()
    if texto:
        adicionar_tarefa(texto)
    return redirect(url_for('index'))

@app.route('/completo/<int:id>')
def marcar_completo(id):
    concluir_tarefa(id)
    return redirect(url_for('index'))

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/tarefas', methods=['POST'])
def adicionar():
    return adicionar_tarefa(request.json['texto'])

@app.route('/tarefas', methods=['GET'])
def listar():
    return listar_tarefas()

@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar(id):
    return atualizar_tarefa(id, request.json['texto'])

@app.route('/tarefas/<int:id>', methods=['PATCH'])
def concluir(id):
    return concluir_tarefa(id)

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def excluir(id):
    return excluir_tarefa(id)

if __name__ == '__main__':
    app.run(debug=True)