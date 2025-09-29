from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html lang='pt-br'>
<head>
	<meta charset='UTF-8'>
	<meta name='viewport' content='width=device-width, initial-scale=1'>
	<title>Calculadora Flask</title>
	<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css' rel='stylesheet'>
	<style>
		body { background: #f8f9fa; }
		.calc-container { max-width: 400px; margin: 40px auto; background: #fff; border-radius: 12px; box-shadow: 0 2px 8px #0001; padding: 32px; }
		.result, .error { margin-top: 20px; }
	</style>
</head>
<body>
	<div class='calc-container'>
		<h2 class='mb-4 text-center'>Calculadora Interativa</h2>
		<form action='/calcular' method='post'>
			<div class='mb-3'>
				<label for='a' class='form-label'>Número A</label>
				<input type='number' step='any' class='form-control' id='a' name='a' placeholder='Digite o primeiro número' required>
			</div>
			<div class='mb-3'>
				<label for='operacao' class='form-label'>Operação</label>
				<select class='form-select' id='operacao' name='operacao'>
					<option value='+'>Somar (+)</option>
					<option value='-'>Subtrair (-)</option>
					<option value='*'>Multiplicar (*)</option>
					<option value='/'>Dividir (/)</option>
				</select>
			</div>
			<div class='mb-3'>
				<label for='b' class='form-label'>Número B</label>
				<input type='number' step='any' class='form-control' id='b' name='b' placeholder='Digite o segundo número' required>
			</div>
			<button type='submit' class='btn btn-primary w-100'>Calcular</button>
		</form>
		{% if resultado is not none %}
			<div class='alert alert-success result text-center'>
				<strong>Resultado:</strong> {{ resultado }}
			</div>
		{% elif erro %}
			<div class='alert alert-danger error text-center'>
				<strong>Erro:</strong> {{ erro }}
			</div>
		{% endif %}
	</div>
	<script src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js'></script>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
	return render_template_string(HTML_FORM, resultado=None, erro=None)

@app.route("/calcular", methods=["POST"])
def calcular():
	a = request.form.get("a", type=float)
	b = request.form.get("b", type=float)
	operacao = request.form.get("operacao")
	resultado = None
	erro = None
	try:
		if operacao == "+":
			resultado = f"{a} + {b} = {a + b}"
		elif operacao == "-":
			resultado = f"{a} - {b} = {a - b}"
		elif operacao == "*":
			resultado = f"{a} * {b} = {a * b}"
		elif operacao == "/":
			if b == 0:
				erro = "Divisão por zero não permitida."
			else:
				resultado = f"{a} / {b} = {a / b}"
		else:
			erro = "Operação inválida."
	except Exception as e:
		erro = str(e)
	return render_template_string(HTML_FORM, resultado=resultado, erro=erro)

if __name__ == "__main__":
	app.run(debug=True)