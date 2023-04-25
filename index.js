function getRandomNumber(size) {
	return Math.floor(Math.random() * size);
}

let width = 600;
let height = 450;

let target = {
	x: getRandomNumber(width),
	y: getRandomNumber(height)
}

console.log(target);

let clicks = 0; // Кол-во кликов

$("#map").click(function(event) {
	clicks++;
	console.log(clicks);
	// Здесь будет обработчик кликов

	// Получаем расстояние от места клика до цели
	let distance = getDistance(event, target);

	// Получаю подсказку на основе расстояния
	let distanceText = getDistanceHit(distance);

	// Вывод на экран полученной подсказки
	$("#distance").text(distanceText);

	if (distance < 8) {
		alert("Клад найден! Сделано кликов: " + clicks);
	}

});

function getDistance(event, target) {
	// Расстояние до цели
	let a = event.offsetX - target.x;
	let b = event.offsetY - target.y;
	let c = Math.sqrt((a * a) + (b * b)) // √(a^2 + b^2)
	return c
}

function getDistanceHit(distance) {
	if (distance < 10) {
		return "Обожгёшься!";
	} else if (distance < 20) {
		return "Очень горячо!";
	} else if (distance < 40) {
		return "Горячо!";
	} else if (distance < 80) {
		return "Тепло!";
	} else if (distance < 160) {
		return "Холодно!";
	} else if (distance < 300) {
		return "Очень холодно";
	} else {
		return "Замёрзнешь!!!";
	}
}
