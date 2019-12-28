const fs = require("fs");
const Day1Solver = require("./day1");

main();

function main() {
    const { day } = parseArgs(process.argv, { defaultDay: 1 });
    const solver = getSolver(day);
    const input = getInput(day);
    console.log("solving...");
    const result = solver.solve(input);
    console.log(result);
}

function parseArgs(args, { defaultDay }) {
    let day = defaultDay;
    for (let i = 0; i < args.length; i++) {
        const currentArg = args[i];
        if (currentArg === "-d") {
            day = parseInt(args[i + 1]);
        }
    }
    return { day };
}

function getSolver(day) {
    switch (day) {
        case 1:
            return Day1Solver;
        default:
            throw Error("not implemented yet");
    }
}

function getInput(day) {
    const textInput = fs.readFileSync(`./input${day}.txt`).toString();
    return textInput.split("\n").filter(string => string !== "");
}