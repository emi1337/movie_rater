fox = ["F", "O", "X"];
guessedLetters = [];


/iterate through the code./ 
guessLetter = function(entryLetter) {
	for(var i=0; i < fox.length; i++) {
		if(fox[i] == entryLetter) {
			guessedLetters.push(entryLetter)
			console.log("You guessed a new letter!")
			console.log(guessedLetters);
		}
}
	if(fox.length == guessedLetters.length) {
		console.log(fox);
		console.log("Congrats, you guessed all the letters!");
	}
	else {
		console.log("You need " + (fox.length - guessedLetters.length) + " more letters!");
	}
}