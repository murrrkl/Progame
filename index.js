let catchMole = document.getElementById('catch');
let lostMole = document.getElementById('lost');

let win = 0;
let lost = 0;

// Функция генерации рандомного числа
const random = (min, max) => {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Помещаю все ячейки в массив holes
let holes = document.querySelectorAll('.hole');

// Создание функции удаления класса hole_has_mole
function del(number) {
	if (holes[number].classList.contains('hole_has_mole')) {
    holes[number].classList.remove('hole_has_mole');         
  } 
}


setInterval(function() {
  // Генерирую рандомное число
	let n = random(0, 8)

	// Добавляю класс hole_has_mole ячейке
	holes[n].classList.add("hole_has_mole");
	setTimeout(del, 700, n);

}, 1000);

for (let i = 0; i < 8; i++) {
  holes[i].onclick = function () {
            
  if (holes[i].classList.contains('hole_has_mole')) {
      holes[i].classList.remove('hole_has_mole');
      win = win + 1;
      catchMole.innerHTML = win;
  } else {
  		lost = lost + 1;
  		lostMole.innerHTML = lost;
  }
            
  };
 }



