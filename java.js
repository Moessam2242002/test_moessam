// Function to generate a random password
function generatePassword(length, useUppercase, useLowercase, useNumbers, useSpecialChars) {
    // Define character sets for each type
    const uppercaseChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const lowercaseChars = 'abcdefghijklmnopqrstuvwxyz';
    const numberChars = '0123456789';
    const specialChars = '!@#$%^&*()-_';

    // Initialize character pool based on selected types
    let chars = '';
    if (useUppercase) chars += uppercaseChars;
    if (useLowercase) chars += lowercaseChars;
    if (useNumbers) chars += numberChars;
    if (useSpecialChars) chars += specialChars;

    // Check if at least one character type is selected
    if (chars.length === 0) {
        console.error('Please select at least one character type.');
        return null;
    }

    // Generate the password
    let password = '';
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * chars.length);
        password += chars[randomIndex];
    }

    return password;
}

// Example usage
const length = 12;
const useUppercase = true;
const useLowercase = true;
const useNumbers = true;
const useSpecialChars = true;

const password = generatePassword(length, useUppercase, useLowercase, useNumbers, useSpecialChars);
console.log('Generated Password:', password);
