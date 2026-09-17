/*// definicion o declaracion
function saludar(){
    console.log("HOLA!!!");
}

//llamar una funcion.
saludar();*/

/*//declaramos funcion con parametros
function sumar(num1, num2){
    let resultado = num1 + num2;
    console.log("El resultado es:" + resultado);
}

//llamar funcion
sumar(14, 20);
sumar(9, 8);
sumar(70, 35);*/

//scope y retornos 
function suma(nota1, nota2, nota3){
    let result = nota1 + nota2 + nota3;
    return result;
}

function promedio(){
    let rdoSuma = suma(7, 9, 8);
    let rdoPromedio = rdoSuma / 3;
    return rdoPromedio;
}

//llamado
let promedioObtenido = promedio();
console.log("El promedio de sus notas es: " + promedioObtenido);