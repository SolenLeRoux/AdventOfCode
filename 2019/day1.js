exports.solve = input => {
    const masses = parse(input);
    let requiredFuel = 0;
    masses.forEach(mass => requiredFuel += exports.computeRequiredFuel(mass));
    return requiredFuel;
};

function parse(input) {
    return input.map(string => parseInt(string));
}

exports.computeRequiredFuel = mass => {
    return Math.floor(mass / 3) - 2;
};
