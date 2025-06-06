/* AREA DO CÍRCULO
var input = require('fs').readFileSync('stdin', 'utf8');

var raio = parseFloat(input)

var pi = 3.14159;

var resultado = pi * Math.pow(raio,2);

console.log('A=' + resultado.toFixed(4));
*/

/* SOMA SIMPLES
var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

var valor1 = parseInt(lines.shift())
var valor2 = parseInt(lines.shift())

var resultado = valor1 + valor2

console.log("SOMA = " + resultado)

*/

/* PRODUTO SIMPLES
var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

var valor1 = parseInt(lines.shift())
var valor2 = parseInt(lines.shift())

var resultado = valor1 * valor2

console.log("PROD = " + resultado)
*/

/* MEDIA 1
var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

var valor1 = parseFloat(lines.shift());
var valor2 = parseFloat(lines.shift());

var resultado = (valor1 * 3.5+ valor2 * 7.5) / 11.0;

var resultado = resultado.toFixed(5);

console.log("MEDIA = " + resultado);
*/

/* MEDIA 2
var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

var valor1 = parseFloat(lines.shift());
var valor2 = parseFloat(lines.shift());
var valor3 = parseFloat(lines.shift());

var resultado = ((valor1 * 2) + (valor2 * 3) + (valor3 * 5)) / 10

var resultado = resultado.toFixed(1)

console.log('MEDIA = ' + resultado)
*/

/* DIFERENÇA
var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

var valor1 = parseInt(lines.shift());
var valor2 = parseInt(lines.shift());
var valor3 = parseInt(lines.shift());
var valor4 = parseInt(lines.shift());

var resultado = (valor1 * valor2)  - (valor3 * valor4);

console.log('DIFERENCA = ' + resultado); 
*/

/* SALARIO
var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

var numero = parseInt(lines.shift());
var horas = parseInt(lines.shift());
var valor = parseFloat(lines.shift());

var salario = valor * horas;
var salario = salario.toFixed(2);

console.log('NUMBER = ' + numero);
console.log('SALARY = U$ ' + salario);

*/

/* SALARIO COM BONUS 
var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

var nome = toString(lines.shift());
var salario = parseFloat(lines.shift());
var vendas = parseFloat(lines.shift());

var bonus = vendas * 0.15;

var tudo = salario + bonus;

console.log('TOTAL = R$ ' + tudo.toFixed(2));
*/

/* CALCULO SIMPLES
var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

var peca1 = lines.shift().split(' ')
var peca2 = lines.shift().split(' ')

var codigo1 = parseInt(peca1.shift());
var unidades1 = parseInt(peca1.shift());
var valor1 = parseFloat(peca1.shift());

var codigo2 = parseInt(peca2.shift());
var unidades2 = parseInt(peca2.shift());
var valor2 = parseFloat(peca2.shift());

somaTotal = (unidades1 * valor1) + (unidades2 * valor2);

console.log('VALOR A PAGAR: R$ ' + somaTotal.toFixed(2));
*/


var input = require('fs').readFileSync('stdin', 'utf8');
var lines = input.split('\n');

var raio = parseInt(lines.shift());
var pi = 3.14159

var volume = (4.0 / 3) * pi * Math.pow(raio, 3)

console.log('VOLUME = ' + volume.toFixed(3));


