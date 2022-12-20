window.addEventListener('load', calculateTime);

function calculateTime() {
	let date = new Date();

	let dayNumber = date.getDay();
	let hour = date.getHours();
	let min = date.getMinutes();
	let ampm;

	if (hour >= 12) {
		ampm = 'PM';
	} else {
		ampm = 'AM';
	}

	let dayNames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

	hour = hour % 12;

	if (hour == 0) {
		hour = 12;
	}

	if (hour < 10) {
		hour = "0" + hour;
	}

	if (min < 10) {
		min = "0" + min;
	}

	document.getElementById("day").innerHTML = dayNames[dayNumber];
	document.getElementById("hour").innerHTML = hour;
	document.getElementById("minute").innerHTML = min;
	document.getElementById("ampm").innerHTML = ampm;


	setTimeout(calculateTime, 200);
}

