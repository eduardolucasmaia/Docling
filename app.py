import os
from flask import Flask, request, jsonify, render_template_string
from werkzeug.utils import secure_filename
import logging
from docling.document_converter import DocumentConverter

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'docx', 'xlsx', 'html', 'md'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# HTML template for the frontend
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Docling Upload</title>
    <style>
        :root {
          --primary-color: #4a6fa5;
          --secondary-color: #6b8cae;
          --accent-color: #2c3e50;
          --light-color: #f8f9fa;
          --dark-color: #343a40;
          --success-color: #28a745;
          --error-color: #dc3545;
          --border-radius: 5px;
          --box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        
        * {
          box-sizing: border-box;
          margin: 0;
          padding: 0;
        }
        
        body {
          font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
          line-height: 1.6;
          color: var(--dark-color);
          background-color: #f5f7fa;
          padding: 20px;
        }
        
        .container {
          max-width: 800px;
          margin: 0 auto;
          background-color: white;
          padding: 30px;
          border-radius: var(--border-radius);
          box-shadow: var(--box-shadow);
        }
        
        h1 {
          color: var(--primary-color);
          margin-bottom: 20px;
          text-align: center;
        }
        
        h2 {
          color: var(--secondary-color);
          margin: 20px 0 10px;
          font-size: 1.3rem;
        }
        
        .form-group {
          margin-bottom: 20px;
        }
        
        label {
          display: block;
          margin-bottom: 8px;
          font-weight: 600;
        }
        
        input[type="file"] {
          display: block;
          width: 100%;
          padding: 10px;
          border: 1px solid #ddd;
          border-radius: var(--border-radius);
          background-color: var(--light-color);
        }
        
        button {
          background-color: var(--primary-color);
          color: white;
          border: none;
          padding: 12px 20px;
          border-radius: var(--border-radius);
          cursor: pointer;
          font-size: 16px;
          font-weight: 600;
          transition: background-color 0.3s;
          margin-right: 10px;
        }
        
        button:hover {
          background-color: var(--accent-color);
        }
        
        .button-group {
          display: flex;
          margin-top: 15px;
        }
        
        #exportButton {
          background-color: var(--success-color);
        }
        
        #exportButton:hover {
          background-color: #218838;
        }
        
        #resultArea {
          margin-top: 30px;
          display: none;
        }
        
        #output {
          background-color: #f8f9fa;
          border: 1px solid #ddd;
          border-radius: var(--border-radius);
          padding: 15px;
          white-space: pre-wrap;
          overflow-x: auto;
          font-family: 'Courier New', Courier, monospace;
          font-size: 14px;
          line-height: 1.5;
          max-height: 500px;
          overflow-y: auto;
        }
        
        #errorArea {
          margin-top: 20px;
          padding: 15px;
          background-color: #fff8f8;
          border: 1px solid var(--error-color);
          border-radius: var(--border-radius);
          display: none;
        }
        
        #errorMessage {
          color: var(--error-color);
        }
        
        /* Spinner para indicação de carregamento */
        #loadingIndicator {
          display: none;
        }
        
        .spinner {
          border: 4px solid rgba(0, 0, 0, 0.1);
          width: 36px;
          height: 36px;
          border-radius: 50%;
          border-left-color: var(--primary-color);
          animation: spin 1s linear infinite;
          margin: 20px auto;
        }
        
        @keyframes spin {
          0% {
            transform: rotate(0deg);
          }
          100% {
            transform: rotate(360deg);
          }
        }
        
        /* Responsividade */
        @media (max-width: 600px) {
          .container {
            padding: 15px;
          }
          
          h1 {
            font-size: 1.5rem;
          }
          
          button {
            width: 100%;
            margin-bottom: 10px;
            margin-right: 0;
          }
          
          .button-group {
            flex-direction: column;
          }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Upload de Documento para Processamento com Docling</h1>
        
        <form id="uploadForm" enctype="multipart/form-data">
            <div class="form-group">
                <label for="fileInput">Selecione um arquivo:</label>
                <input type="file" id="fileInput" name="file" required>
            </div>
            <button type="submit" id="submitButton">Enviar e Processar</button>
        </form>

        <div id="loadingIndicator">
            <p>Processando, por favor aguarde...</p>
            <div class="spinner"></div> 
        </div>

        <div id="resultArea">
            <h2>Resultado do Processamento (Markdown):</h2>
            <pre id="output"></pre>
            
            <div class="button-group">
                <button id="exportButton">Exportar Markdown</button>
                <button id="copyButton">Copiar para Área de Transferência</button>
            </div>
        </div>

        <div id="errorArea">
            <h2>Erro:</h2>
            <p id="errorMessage"></p>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const uploadForm = document.getElementById('uploadForm');
            const fileInput = document.getElementById('fileInput');
            const submitButton = document.getElementById('submitButton');
            const loadingIndicator = document.getElementById('loadingIndicator');
            const resultArea = document.getElementById('resultArea');
            const output = document.getElementById('output');
            const errorArea = document.getElementById('errorArea');
            const errorMessage = document.getElementById('errorMessage');
            const exportButton = document.getElementById('exportButton');
            const copyButton = document.getElementById('copyButton');
            
            let currentMarkdown = "";
        
            // Função para mostrar mensagem de erro
            function showError(message) {
                errorMessage.textContent = message;
                errorArea.style.display = 'block';
                resultArea.style.display = 'none';
                loadingIndicator.style.display = 'none';
                submitButton.disabled = false;
            }
        
            // Função para mostrar resultado
            function showResult(markdownContent) {
                currentMarkdown = markdownContent;
                output.textContent = markdownContent;
                resultArea.style.display = 'block';
                errorArea.style.display = 'none';
                loadingIndicator.style.display = 'none';
                submitButton.disabled = false;
            }
            
            // Função para exportar markdown como arquivo .md
            function exportMarkdown() {
                if (!currentMarkdown) {
                    showError('Nenhum conteúdo para exportar.');
                    return;
                }
                
                // Criar um blob com o conteúdo markdown
                const blob = new Blob([currentMarkdown], { type: 'text/markdown' });
                
                // Criar um URL temporário para o blob
                const url = URL.createObjectURL(blob);
                
                // Criar um elemento de link para download
                const a = document.createElement('a');
                a.href = url;
                
                // Usar o nome do arquivo original ou um nome padrão
                const originalFileName = fileInput.files[0]?.name || 'documento';
                const baseFileName = originalFileName.split('.')[0] || 'documento';
                a.download = `${baseFileName}_processado.md`;
                
                // Adicionar o link ao documento, clicar nele e removê-lo
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                
                // Liberar o URL do objeto
                URL.revokeObjectURL(url);
            }
            
            // Função para copiar markdown para a área de transferência
            function copyToClipboard() {
                if (!currentMarkdown) {
                    showError('Nenhum conteúdo para copiar.');
                    return;
                }
                
                navigator.clipboard.writeText(currentMarkdown)
                    .then(() => {
                        // Feedback visual temporário
                        const originalText = copyButton.textContent;
                        copyButton.textContent = 'Copiado!';
                        copyButton.style.backgroundColor = 'var(--success-color)';
                        
                        setTimeout(() => {
                            copyButton.textContent = originalText;
                            copyButton.style.backgroundColor = 'var(--primary-color)';
                        }, 2000);
                    })
                    .catch(err => {
                        showError('Erro ao copiar: ' + err);
                    });
            }
        
            // Manipulador de evento para o envio do formulário
            uploadForm.addEventListener('submit', function(event) {
                event.preventDefault();
                
                // Verificar se um arquivo foi selecionado
                if (!fileInput.files || fileInput.files.length === 0) {
                    showError('Por favor, selecione um arquivo para upload.');
                    return;
                }
        
                const file = fileInput.files[0];
                
                // Criar FormData para enviar o arquivo
                const formData = new FormData();
                formData.append('file', file);
                
                // Mostrar indicador de carregamento e desabilitar botão
                loadingIndicator.style.display = 'block';
                resultArea.style.display = 'none';
                errorArea.style.display = 'none';
                submitButton.disabled = true;
                
                // Enviar requisição para o backend
                fetch('/upload', {
                    method: 'POST',
                    body: formData
                })
                .then(response => {
                    if (!response.ok) {
                        // Se a resposta não for OK (200), lançar erro
                        return response.json().then(data => {
                            throw new Error(data.error || 'Erro desconhecido no servidor');
                        });
                    }
                    return response.json();
                })
                .then(data => {
                    // Processar resposta bem-sucedida
                    if (data.markdown) {
                        showResult(data.markdown);
                    } else {
                        showError('Resposta do servidor não contém dados Markdown.');
                    }
                })
                .catch(error => {
                    // Processar erros
                    showError(`Erro: ${error.message}`);
                    console.error('Erro durante o upload:', error);
                });
            });
        
            // Limpar mensagens de erro quando um novo arquivo é selecionado
            fileInput.addEventListener('change', function() {
                errorArea.style.display = 'none';
                resultArea.style.display = 'none';
            });
            
            // Adicionar event listeners para os botões de exportação e cópia
            exportButton.addEventListener('click', exportMarkdown);
            copyButton.addEventListener('click', copyToClipboard);
        });
    </script>
</body>
</html>
'''

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/status')
def status():
    return jsonify({"status": "API funcionando corretamente"})

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        logger.warning("No file part in the request")
        return jsonify({"error": "Nenhum arquivo selecionado"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        logger.warning("No selected file")
        return jsonify({"error": "Nenhum arquivo selecionado"}), 400

    if file and allowed_file(file.filename):
        # Use secure_filename for security
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        try:
            logger.info(f"Saving file to {filepath}")
            file.save(filepath)
            logger.info(f"File saved successfully: {filename}")

            # Process with Docling
            logger.info(f"Processing file with Docling: {filepath}")
            converter = DocumentConverter()
            result = converter.convert(filepath)
            logger.info(f"Docling processing complete for: {filename}")

            # Export to Markdown
            markdown_output = result.document.export_to_markdown()
            logger.info(f"Markdown export successful for: {filename}")

            # Clean up the uploaded file
            os.remove(filepath)
            logger.info(f"Removed temporary file: {filepath}")

            return jsonify({"markdown": markdown_output})

        except Exception as e:
            logger.error(f"Error processing file {filename}: {e}", exc_info=True)
            # Clean up the file even if an error occurs
            if os.path.exists(filepath):
                try:
                    os.remove(filepath)
                    logger.info(f"Removed temporary file after error: {filepath}")
                except OSError as remove_error:
                    logger.error(f"Error removing file {filepath} after processing error: {remove_error}")
            return jsonify({"error": f"Erro ao processar o arquivo: {str(e)}"}), 500
    else:
        # File extension not allowed
        logger.warning(f"File extension not allowed: {file.filename}")
        return jsonify({"error": f"Tipo de arquivo não permitido. Extensões permitidas: {', '.join(ALLOWED_EXTENSIONS)}"}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
