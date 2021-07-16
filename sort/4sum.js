/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    nums.sort((a, b) => a - b);
    let res = [];
    
    for(let i = 0; i < nums.length - 3; i++) {
        for(let j = i + 1; j < nums.length - 2; j++) {
            let start = j + 1;
            let end = nums.length - 1;
            while(start < end) {
                let sum = nums[i] + nums[j] + nums[start] + nums[end];
                if(sum === target) {
                    res.push([nums[i], nums[j], nums[start], nums[end]]);
                    while(nums[start + 1] === nums[start]) start++;
                    while(nums[end - 1] === nums[end]) end--;
                    start++;
                    end--;
                } else if(sum < target) {
                    start++;
                } else if(sum > target) {
                    end--;
                }
            }
            while(nums[j+1] === nums[j]) j++
        }
        while(nums[i+1] === nums[i]) i++
    }
    return res;
};
