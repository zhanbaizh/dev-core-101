function findDivisorsOrPrime(num) {
    // Array to store divisors
    let divisors = [];

    // Check for divisors from 2 to num-1
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) {
            divisors.push(i);
            if (i !== num / i) {  // Check for divisors pair
                divisors.push(num / i);
            }
        }
    }

    // If no divisors found, the number is prime
    if (divisors.length === 0) {
        return `${num} is a prime number`;
    } else {
        return `Divisors of ${num} are: ${divisors.sort((a, b) => a - b)}`;
    }
}

// Test the function with a number
console.log(findDivisorsOrPrime(29)); // Output: 29 is a prime number
console.log(findDivisorsOrPrime(24)); // Output: Divisors of 24 are: 2, 3, 4, 6, 8, 12
