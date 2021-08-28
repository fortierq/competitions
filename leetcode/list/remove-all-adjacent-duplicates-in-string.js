var removeDuplicates = function(s) {
    let stack = [];
    for (let c of s) {
        stack.push(c);
        if (stack.length > 1 && stack[stack.length - 1] == stack[stack.length - 2]) {
            stack.pop();
            stack.pop();
        }
    }
    return stack.join('');
};
