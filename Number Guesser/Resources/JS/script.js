let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;


//This function return a random integer between 0 and 9;
const generateTarget = () => {
    return Math.floor(Math.random() * 10);
};

//Convert difference between guesses and target to absolute numbers and compare them, then return true if user wins or false if computer wins;    game.js line26
const compareGuesses = (userGuess, computerGuess, target) => {
    if (userGuess < 0 || userGuess > 9) {
        return alert("Insert number between 0 and 9");
    };
    const userG = Math.abs(userGuess - target);
    const computerG = Math.abs(computerGuess - target);
    return userG <= computerG;
};

//update the score 
const updateScore = winner => {
    if (winner === "human") {
        humanScore += 1;
    } else if (winner === "computer") {
        computerScore += 1;
    }
};

// increase the var currentRoundNumber by 1
const advanceRound = () => {
    currentRoundNumber++;
}