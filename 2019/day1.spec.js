import test from "ava";

import { solve } from "./day1";

test("should return 2 when input is 12", t => {
    const solution = solve(12);
    
    t.is(solution, 2);
});

test("should return 2 when input is 14", t => {
    const solution = solve(14);
    
    t.is(solution, 2);
});

test("should return 654 when input is 1969", t => {
    const solution = solve(1969);
    
    t.is(solution, 654);
});

test("should return 33583 when input is 100756", t => {
    const solution = solve(100756);
    
    t.is(solution, 33583);
});
